# 최대 가로수 10000개 101* 101 개의 소용돌이 먼저 구현

r1, c1, r2 , c2 = map(int, input().split())
SIZE = 10003
A = [[0 for x in range(SIZE+1)] for y in range(SIZE+1)]


# 소용돌이 그리기
# n*n 크기에서 마지막 (n-1,n-1)부터 그리기 시작
# 서 -> 북 -> 동 -> 남 으로 이동

def is_range(x, y):
    return 0 <= x < SIZE and 0 <= y < SIZE

def is_forward(x, y):
    return A[y][x] == 0 and (0 <= x < SIZE and 0 <= y < SIZE)


def drawTable():
    x, y, num, idx = SIZE-1, SIZE-1, SIZE*SIZE, 0
    dx, dy = [-1,0,1,0], [0,-1,0, 1]
    A[y][x] = num
    
    while num >= 1:
        while True:
            A[y][x] = num
            num -= 1
            if not is_forward(x+dx[idx], y+dy[idx]): 
                break
            x, y = x+dx[idx], y+dy[idx]
            
        idx = (idx+1)%4
        x, y = x+dx[idx], y+dy[idx]
        
drawTable()



for y in range(r1+SIZE//2, r2+SIZE//2+1):
    for x in range(c1+SIZE//2, c2+SIZE//2+1):
        print(A[y][x], end= ' ')
    print()