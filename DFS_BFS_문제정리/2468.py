import sys
from collections import deque
input = sys.stdin.readline

l = int(input())
lake = [[int(x) for x in input().split()] for _ in range(l)]

# 범위 확인
def is_range(x, y, l):
    return 0 <= x < l and 0 <= y < l

# 안전 구역의 개수를 반환하는 함수
def bfs(A, l, rain):
    # 물에 잠긴 지격은 0으로 표시
    for y in range(l):
        for x in range(l):
            if A[y][x] <= rain: A[y][x] = 0
            
    
    count = 0
    dx, dy = [1,0,-1,0], [0,1,0,-1]
    
    for y in range(l):
        for x in range(l):
            # 0이 아니라면 bfs 시작
            if A[y][x] != 0:
                queue = deque([(x, y)])
                visited = [[0 for x in range(l+1)] for y in range(l+1)]
                while queue:
                    x, y = queue.popleft()
                    A[y][x] = 0
                    visited[y][x] = 1
                    for i in range(4):
                        ddx, ddy = x+dx[i], y+dy[i]
                        if is_range(ddx, ddy, l) and A[ddy][ddx] != 0 and visited[ddy][ddx] != 1:
                            queue.append((ddx, ddy))
                count += 1
    return count
    
def solution(lake, l):
    result = 0
    max_v = max(map(max, lake))
    for i in range(1, max_v+1):
        result = max(result, bfs(lake, l, i))
    return result

print(solution(lake, l))