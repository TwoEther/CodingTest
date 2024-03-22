n, m = map(int, input().split())
A = [[int(x) for x in input().split()] for y in range(n)]
wall = []
vir = []
ret = 0

def is_range(x, y):
    return 0 <= x < m and 0 <= y < n

def dfs(x, y, visited):
    dx, dy = [1,0,-1,0], [0,1,0,-1]
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if not is_range(nx, ny): continue
        if visited[ny][nx] == 1: continue
        if A[ny][nx] == 1: continue
        
        visited[ny][nx] = 1
        dfs(nx, ny, visited)
        

def go():
    visited = [[0 for x in range(10)] for y in range(10)]

    for v in vir:
        visited[v[1]][v[0]] = 1
        dfs(v[0], v[1], visited)
    
    cnt = 0
    
    for y in range(n):
        for x in range(m):
            if A[y][x] == 0 and visited[y][x] == 0:cnt += 1
    return cnt

for y in range(n):
    for x in range(m):
        if A[y][x] == 0:wall.append((x,y))
        elif A[y][x] == 2: vir.append((x,y))
        
for l in range(len(wall)):
    for y in range(l):
        for x in range(y):
            A[wall[l][1]][wall[l][0]] = 1
            A[wall[y][1]][wall[y][0]] = 1
            A[wall[x][1]][wall[x][0]] = 1
            
            ret = max(ret, go())
            
            A[wall[l][1]][wall[l][0]] = 0
            A[wall[y][1]][wall[y][0]] = 0
            A[wall[x][1]][wall[x][0]] = 0
            
print(ret)