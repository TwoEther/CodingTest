from collections import deque
from itertools import permutations

def solution(board, sr, sc):
    source = [[] for x in range(6)]
    for y in range(5):
        for x in range(5):
            if board[y][x] > 0:
                source[board[y][x]-1] = [y, x]
                
    answer = -1
    for target in permutations(source):
        ret = 0
        r, c = sr, sc 
        for nr, nc in target:
            x = get_move_count(board, r, c, nr, nc)

            if x == -1: 
                ret = -1
                break
            ret += x
            r, c = nr, nc
        if ret != -1:
            if answer == -1 or answer > ret: answer = ret
    
    return answer

def is_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5 

def get_move_count(board, sr, sc, tr, tc):
    queue = deque([(sr, sc)])
    dist = [[0 for x in range(5)] for y in range(5)]
    visited = [[0 for x in range(5)] for y in range(5)]
    dd = [(1,0), (0,-1), (-1,0), (0,1)]
    
    while queue:
        r, c = queue.popleft()
        if r == tr and c == tc: return dist[r][c]
    
        for dr, dc in dd:
            nr, nc = r+dr, c+dc
            if is_range(nr, nc) and visited[nr][nc] == 0 and board[nr][nc] != -1:
                queue.append((nr, nc))
                dist[nr][nc] = dist[r][c] + 1
                visited[nr][nc] = 1
    return -1

board = [[int(x) for x in input().split()] for y in range(5)]
cx, cy = map(int, input().split())
print(solution(board, cx, cy))