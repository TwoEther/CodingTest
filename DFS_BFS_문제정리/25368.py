

def solution(board, play1, play2):
    return solve(board, play1, play2, 0)

# apple_diff : 현재까지 이번 차례 학생이 먹은 사과 개수 - 다음 차례 학생이 먹은 사과 개수
def solve(board, play1, play2, apple_diff):
    # 두 학생 모두 이동할 수 없는 경우 종료
    if board[play1[0]][play1[1]] == -1 and board[play2[0]][play2[1]] == -1:
        if apple_diff > 0: return 1
        return 0

    # 모든 사과를 다 먹은 경우
    remained_apple = 0
    for i in range(5):
        remained_apple += board[i].count(1)
    if remained_apple == 0:
        if apple_diff > 0: return 1
        return 0
    
    dd = [[1,0],[0,-1],[-1,0],[0,1]]
    # 상, 하, 좌, 우 방향으로 시도한 횟수
    try_count = 0
    
    for dx, dy in dd:
        # (r,c) : 다음 이동 위치
        # (r,c) : 위치로 이동 가능한 경우 이동
        r, c = play1[0] + dx, play1[1] + dy
        if is_range(r, c) and board[r][c] != -1 and [r, c] != play2:
            # 시도 횟수를 1 증가 시킴
            # prv_value : 이번 차례 학생의 현재 위치 값을 저장
            # 이번 차례 학생이 (r,c)로 이동한 후에 다음 차례 학생이 이동
            try_count += 1
            prv_value = board[play1[0]][play1[1]]
            board[play1[0]][play1[1]] = -1
            result = solve(board, play2, [r, c], -(apple_diff + board[r][c])+1)

            # 백트래킹
            board[play1[0]][play1[1]] = prv_value
            
            # 다음 차례 학생이 지는 경우 이번차례 학생이 이김
            if result == 0:
                return 1
    
    if try_count == 0:
        prv_value = board[play1[0]][play1[1]]
        board[play1[0]][play1[1]] = -1
        result = solve(board, play2, play1, -apple_diff+1)

        # 백트래킹
        board[play1[0]][play1[1]] = prv_value
        
        if result == 0:
            return 1

    return 0
        
def is_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5


board = [[int(x) for x in input().split()] for y in range(5)]
player = [int(x) for x in input().split()]
play1, play2 = player[0:2], player[2:]
print(solution(board, play1, play2))