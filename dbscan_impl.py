#!/usr/bin/env python3
"""dbscan_impl - DBSCAN clustering algorithm."""
import sys, random, math
def dist(a, b): return math.sqrt(sum((ai-bi)**2 for ai,bi in zip(a,b)))
def dbscan(X, eps=0.5, min_pts=5):
    n=len(X); labels=[-1]*n; cluster=0
    def region_query(i): return [j for j in range(n) if dist(X[i],X[j])<=eps]
    def expand(i, neighbors, c):
        labels[i]=c; queue=list(neighbors)
        while queue:
            q=queue.pop(0)
            if labels[q]==-1: labels[q]=c
            if labels[q]!=-1 and labels[q]!=c: continue
            labels[q]=c
            q_neighbors=region_query(q)
            if len(q_neighbors)>=min_pts: queue.extend(q_neighbors)
    for i in range(n):
        if labels[i]!=-1: continue
        neighbors=region_query(i)
        if len(neighbors)<min_pts: labels[i]=-2  # noise
        else: expand(i, neighbors, cluster); cluster+=1
    return labels, cluster
if __name__=="__main__":
    random.seed(42)
    X = [(random.gauss(0,0.5), random.gauss(0,0.5)) for _ in range(30)] +         [(random.gauss(3,0.5), random.gauss(3,0.5)) for _ in range(30)] +         [(random.uniform(-5,8), random.uniform(-5,8)) for _ in range(10)]
    labels, n_clusters = dbscan(X, eps=1.0, min_pts=3)
    print(f"Clusters: {n_clusters}, Noise: {labels.count(-2)}")
    from collections import Counter
    print(Counter(labels))
