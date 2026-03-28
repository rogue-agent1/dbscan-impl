#!/usr/bin/env python3
"""DBSCAN clustering — zero-dep implementation."""
import math

def euclidean(a,b): return math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))

def dbscan(X, eps=0.5, min_pts=5):
    n=len(X); labels=[-1]*n; cluster=-1; visited=[False]*n
    def region_query(i): return [j for j in range(n) if euclidean(X[i],X[j])<=eps]
    def expand(i, neighbors, c):
        labels[i]=c; queue=list(neighbors)
        while queue:
            j=queue.pop(0)
            if not visited[j]:
                visited[j]=True
                nb=region_query(j)
                if len(nb)>=min_pts: queue.extend(nb)
            if labels[j]==-1: labels[j]=c
    for i in range(n):
        if visited[i]: continue
        visited[i]=True
        neighbors=region_query(i)
        if len(neighbors)<min_pts: labels[i]=-1
        else: cluster+=1; expand(i, neighbors, cluster)
    return labels

if __name__=="__main__":
    import random; random.seed(42)
    X=[]
    for cx,cy in [(0,0),(5,5),(10,0)]:
        X.extend([[cx+random.gauss(0,0.5),cy+random.gauss(0,0.5)] for _ in range(20)])
    X.extend([[random.uniform(-2,12),random.uniform(-2,7)] for _ in range(5)])
    labels=dbscan(X,eps=1.5,min_pts=3)
    clusters=set(labels)-{-1}
    print(f"Found {len(clusters)} clusters, {labels.count(-1)} noise points")
    for c in sorted(clusters): print(f"  Cluster {c}: {labels.count(c)} points")
