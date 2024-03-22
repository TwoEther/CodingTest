from collections import deque
A = [[int(x) for x in input().split()] for _ in range(5)]
r, c = map(int, input().split())

def findOnePoint(A):
    for y in range(5):
        for x in range(5):
            if A[y][x] == 1: return x, y

def is_range(x, y):
    return 0 <= x <= 4 and 0 <= y <= 4

def solution(A, cx, cy):
    tx, ty = findOnePoint(A)
    queue = deque([(cx, cy)])
    visited = [[0 for _ in range(5)] for _ in range(5)]
    dist = [[0 for _ in range(5)] for _ in range(5)]
    dx, dy = [1,0,-1,0], [0,1,0,-1]
    
    
    while queue:
        x, y = queue.popleft()
        
        if x == tx and y == ty: return dist[y][x]
        
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            
            if not is_range(ddx, ddy): continue
            
            if A[ddy][ddx] != -1 and visited[ddy][ddx] == 0:
                dist[ddy][ddx] = dist[y][x] + 1
                queue.append((ddx, ddy))
                visited[ddy][ddx] = 1
    return -1

print(solution(A, c, r))