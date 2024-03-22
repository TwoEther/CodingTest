import itertools
from collections import deque

n, m = map(int, input().split())
A = [[int(x) for x in input().split()] for y in range(n)]
wall = []
vir = []
ret = int(10e9)

def is_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(queue, visited):
    dx, dy = [1,0,-1,0], [0,1,0,-1]
    
    while queue:
        x, y, d = queue.popleft()
        visited[y][x] = d
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not is_range(nx, ny): continue
            if visited[ny][nx] != 0: continue
            if A[ny][nx] == 1: continue
                        
            
            queue.append((nx,ny,d+1))

def go(queue):
    visited = [[0 for x in range(n)] for y in range(n)]    
    bfs(queue, visited)
    
    cnt = 0
    
    for y in range(n):
        for x in range(n):
            if visited[y][x] == 0 and A[y][x] != 1: return int(10e9)
            cnt = max(cnt, visited[y][x])
    return cnt

for y in range(n):
    for x in range(n):
        if A[y][x] == 2: vir.append((x,y))
    
_comb = list(itertools.combinations(vir, m))
        
for com in _comb:
    queue = deque([])
    for l in com:
        x, y = l
        A[y][x] = 3
        queue.append((x, y, 0)) 
    ret = min(ret, go(queue))
    
    for l in com:
        x, y = l
        A[y][x] = 2
    
print(-1 if ret == int(10e9) else ret)