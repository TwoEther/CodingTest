from collections import deque
t = int(input())

def is_range(l, x, y):
    return 0 <= x < l and 0 <= y < l

def bfs(l, sx, sy, cx, cy):
    queue = deque([(sx, sy)])
    visited = [[0 for x in range(l)] for y in range(l)]
    dd = [(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2)]
    visited[sy][sx] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            dx, dy = x+dd[i][0], y+dd[i][1]
            if is_range(l, dx, dy) and visited[dy][dx] == 0:
                visited[dy][dx] = visited[y][x] + 1
                queue.append((dx, dy))
            if dx == cx and dy == cy: return visited[dy][dx]-1
            
    return -1

def solution(l, sx, sy, cx, cy):
    return bfs(l, sx, sy, cx, cy)

for _ in range(t):
    l = int(input())
    sx, sy = map(int, input().split())
    cx, cy = map(int, input().split())

    print(solution(l, sx, sy, cx, cy))
    
    