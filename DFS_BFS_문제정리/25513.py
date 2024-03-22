from collections import deque

A = [[int(x) for x in input().split()] for y in range(5)]
sr, sc = map(int, input().split())

def solution(A, sx, sy):
    # 1~6 이 적혀 있는 칸의 위치를 target에 저장
    target = list([] for _ in range(6))
    for y in range(5):
        for x in range(5):
            if A[y][x] > 0:
                target[A[y][x]-1] = [x, y]
                
    answer = 0
    for nx, ny in target:
        ret = get_move_count(A, sx, sy, nx, ny)
        if ret == -1: return -1
        
        answer += ret
        
    return answer

# A[y][x] 에서 A[ny][nx]까지의 최단거리
def get_move_count(A, sx, sy, tx, ty):
    dx, dy = [1,0,-1,0], [0,1,0,-1]
    visited = [[0]*5 for _ in range(5)]
    dist = [[0]*5 for _ in range(5)]
    
    queue = deque([(sx, sy)])
    visited[sy][sx] = 1
    dist[sy][sx] = 0
    while queue:
        x, y = queue.popleft()
        
        if y == ty and x == tx: return dist[ty][tx]
        
        for i in range(4):
            ddx = dx[i] + x
            ddy = dy[i] + y
            
            if in_range(ddx, ddy) and visited[ddy][ddx] == 0 and A[ddy][ddx] != -1:
                queue.append((ddx, ddy))
                dist[ddy][ddx] = dist[y][x] + 1
                visited[ddy][ddx] = 1
    return -1
            
def in_range(x, y):
    return 0 <= x <= 4 and 0 <= y <= 4
    
print(solution(A, sc, sr))