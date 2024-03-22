import sys
from collections import deque


def solution():
    n, k = map(int, input().split())
    tree = [[] for _ in range(n+1)]


    for _ in range(n):
        e, d = map(int, input().split())
        tree[e].append(d)
        tree[d].append(e)
        
    
    nodes = [int(x) for x in input().split()]
    visited = [0]*(n+1)
    
    queue = deque([(0,0)])
    
    while queue:
        v, d = queue.popleft()
        visited[v] = 1
        
        if v == k: return d
        
        for x in tree[v]:
            if visited[v] != 0:
                queue.append((x, d+1))
    return -1

print(solution())
    