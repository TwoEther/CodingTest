import sys
input = sys.stdin.readline
test_case = int(input())

for t in range(test_case):
    n = int(input())
    cards = [int(x) for x in input().split()]
    dp = [[0,0] * (n+1)]
    
    dp[1][0] = dp[1][1] = cards[0]
    dp[2][0] = dp[1][0]
    dp[2][1] = dp[1][0] + cards[1]
    
    for i in range(3, n+1):
        dp[i][0] = dp[i-2] + 2 *(cards[i-1]+dp[i-1])
        dp[i][1] = dp[i-1][1] + cards[i-1]
    print(dp[n])