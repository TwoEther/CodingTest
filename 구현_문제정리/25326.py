n, m = map(int, input().split())
likes = [[x for x in input().split()] for _ in range(n)]
questions = [[x for x in input().split()] for _ in range(m)]

# 사전에 상수 딕셔너리로 정의
d = {'-' : 0, 'kor' : 1, 'eng' : 2, 'math': 3,
    'apple' : 1, 'pear' : 2, 'orange' : 3,
    'red' : 1, 'blue' : 2, 'green' : 3}

def is_ok(query, student):
    for i in range(3):
        if query[i] != 0 and query[i] != student[i]:return False
    return True

score = [[[0] * 4 for _ in range(4)] for _ in range(4)]

for s, f, c in likes:
    for subject in range(4):
        for fruit in range(4):
            for color in range(4):
                if is_ok([subject, fruit, color], [d[s], d[f], d[c]]): score[subject][fruit][color] += 1

answer = []
for subject, fruit, color in questions:
    answer.append(score[d[subject]][d[fruit]][d[color]])

for a in answer: print(a)
