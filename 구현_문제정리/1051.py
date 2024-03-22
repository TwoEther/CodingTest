n, m = map(int, input().split())
A = [[int(x) for x in input()] for y in range(n)]

def findVertexInTable(l):
    for y in range(n-l+1):
        for x in range(m-l+1):
            if A[y][x] == A[y+l-1][x+l-1] == A[y][x+l-1] == A[y+l-1][x]: return l*l
    return 1

def solution():
    result = 1
    length = min(n, m)
    
    # length ~ 2 까지 꼭지점 탐색
    for case in range(length,1,-1):
        result = findVertexInTable(case)
        if result != 1: 
            break
    print(result)
solution()