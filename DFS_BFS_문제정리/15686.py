# 로직
# 모든 치킨 거리를 구하는 문제
# 1. 치킨집 M개에 대해 리스트 저장
from itertools import combinations
from collections import deque

n, m = map(int, input().split())
table = [[int(x) for x in input().split()] for y in range(n)]
dist = [[int(10e9) for x in range(n)] for y in range(n)]
chicken, cities = [], []

for y in range(n):
    for x in range(n):
        if table[y][x] == 2: chicken.append((x,y))
        elif table[y][x] == 1: cities.append((x,y))
        else: pass

def is_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(visited):
    dd = [(1,0), (0,-1), (-1,0), (0,1)]
            
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx = x + dd[i][0]
            dy = y + dd[i][1]
            if not is_range(dx, dy): continue
            if visited[dy][dx] == 0:
                visited[dy][dx] = visited[y][x] + 1
                queue.append((dx, dy))
    return visited
    
            
def findChickenLength():
    length = 0
    
    visited = [[0 for x in range(n)] for y in range(n)]
    
    visited = bfs(visited, chicken)
    
    for city in cities:
        x, y = city
        length += visited[y][x]
    return length

def solution():
    answer = int(10e9)
    for chick in chicken:
        x, y = chick
        table[y][x] = 0
            
    # 1개만 영엽하는 경우
    for chick in chicken:
        x, y = chick
        table[y][x] = 2

        answer = min(answer, findChickenLength())
        
        table[y][x] = 0   
    
    for i in range(2, m+1):
        comb = list(combinations(chicken, i))
        for comb in comb:
            for d in comb:
                x, y = d
                table[y][x] = 2
        
                answer = min(answer, findChickenLength())
                
                table[y][x] = 0  
    return answer
print(solution())