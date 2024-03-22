n = int(input())
T = [0 for x in range(n+1)]
P = [0 for x in range(n+1)]
dp = [0 for y in range(n+1)]
for i in range(1, n+1):
    t, p = map(int, input().split())
    T[i], P[i] = t, p

for k in range(1, n+1):
    if k+T[k] >= n+1: continue
    dp[k+T[k]] = max(dp[k+T[k]], dp[k]+P[k])
print(max(dp))
    