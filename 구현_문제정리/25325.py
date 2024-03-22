n = int(input())
students = [_ for _ in input().split()]
student_dict = dict(zip(students, [0]*len(students)))

for _ in range(n):
    for s in input().split():
        student_dict[s] += 1

for key, value in sorted(student_dict.items(), key=lambda x:(-x[1], x[0])):
    print(key, value)