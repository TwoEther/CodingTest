from collections import deque

m, n = map(int, input().split())
board = [[int(x) for x in input().split()] for y in range(n)]
tomato = deque([])

for y in range(n):
    for x in range(m):
        if board[y][x] == 1:
            tomato.append((x,y))

def is_range(x, y):
    return 0 <= x < m and 0 <= y < n

def solution():
    return bfs()

def is_ripe():
    count = 0
    for y in range(n):
        count += board[y].count(0)
    return count == 0

def is_remained():
    for y in range(n):
        for x in range(m):
            if board[y][x] == 0:
                return False
    return True

def bfs():
    if is_ripe(): return 0     
    
    dd = [(1,0),(0,-1),(-1,0),(0,1)]
    while tomato:
        x, y = tomato.popleft()
        for i in range(4):
            dx = x + dd[i][0]
            dy = y + dd[i][1]
            
            if is_range(dx, dy) and board[dy][dx] == 0:
                board[dy][dx] = board[y][x] + 1
                tomato.append((dx, dy))
    
    if not is_remained(): return -1       
    else: return max(map(max, board))-1

print(solution())