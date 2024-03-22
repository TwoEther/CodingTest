import math
n = int(input())
time_dict = {}
base_time, base_cost, per_time, per_cost = 100, 10, 50, 3

def convertTime(time):
    h, m = map(int, time.split(':'))
    return h*60 + m

for _ in range(n):
    time, stu = map(str, input().split())
    call_time = convertTime(time)
    
    if time_dict.get(stu) == None: time_dict[stu] = call_time
    else: time_dict[stu] += call_time
    
for key in time_dict.keys():
    target = time_dict[key]
    if target <= base_time: target = base_cost
    else: target = base_cost + math.ceil((target-base_time) / per_time) * per_cost
    time_dict[key] = target
    
for key, item in sorted(time_dict.items(), key=lambda x:(-x[1],x[0])):
    print(key, item)