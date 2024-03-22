from itertools import combinations
x = input()
y = input()
z = input()
k = int(input())
word_dict = {}
answer = []

def solution(X, Y, Z, k):
    x = list(map("".join, (combinations(X, k))))
    y = list(map("".join, (combinations(Y, k))))
    z = list(map("".join, (combinations(Z, k))))
    
    d = {}
    solve(x, d)
    solve(y, d)
    solve(z, d)
    
    answer = []
    for key, value in d.items():
        if value >= 2: answer.append(key)
    answer.sort()
    
    if len(answer) == 0:
        answer = [-1]
    return answer

def solve(C, d):
    for c in C:
        if c in d:
            d[c] += 1
        else: d[c] = 1


C = solution(x,y,z,k)
for c in C:print(c)