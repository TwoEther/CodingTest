n = int(input())



def solution(n):
    dp = [[0]*10 for _ in range(n+1)]
    for j in range(1, 10): dp[1][j] = 1
    
    for i in range(2, n+1):
        for j in range(1, 10):
            s = max(j-2, 1)
            e = min(j+2, 9)
            
            for k in range(s, e+1):
                dp[i][j] += dp[i-1][k]
            dp[i][j] %= 987654321

    answer = 0
    for j in range(1, 10): answer += dp[n][j]
    return answer % 987654321


print(solution(n))