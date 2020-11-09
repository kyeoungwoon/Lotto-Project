import random

# full = dict()
# for i in range(45):
#     full.setdefault(str(i+1), 0)

# time = int(input())
# for i in range(time):
#     turn = random.sample(range(1,46), 6)
#     for turns in turn:
#         full[str(turns)] += 1

    
# def getValue(x):
#     return full.values()

# for i in range(6):
#     result = list()
#     result.add(max(full.values))

##

full = list()
for i in range(45):
    full.append([i, 0])

n = int(input())
for i in range(n):
    turn = random.sample(range(45), 6)
    for turns in turn:
        full[turns][1]+=1

result = [0, 0, 0, 0, 0, 0]
print(full)
print(full.sort())