n, k = map(int, input().split())
ban = [int(x) for x in input().split()]

def solution(n, k, ban):
    B = [0] * (n+1)
    for b in ban:
        B[b] = 1
    
    dp = [0] * (n+2)
    for i in range(n, 0, -1):
        # 현재 학생이 i ~ i+k-1 까지 외칠수 있다.
        for j in range(i, i+k):
            if j > n: break
            
            # j를 외칠 수 없는 경우
            if B[j] == 1: continue
            
            # 현재 학생이 j를 외치고 다음 학생이 지는 경우
            if dp[j+1] == 0:
                dp[i] = 1
                break
    return dp[1]

print(solution(n,k,ban))