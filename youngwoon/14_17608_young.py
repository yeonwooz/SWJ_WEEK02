# 막대기 17608
import sys
input = sys.stdin.readline
n = int(input())

stick = [int(input()) for _ in range(n)]

see = [stick[n-1]]# 7 6
standard = stick[n-1]
for i in range(n):
    if stick[n -1 - i] > standard:
        see.append(max(see[len(see)-1], stick[n -1 - i])) # 8
answer = set(see)
# print(answer)
print(len(answer))

# stack = [int(input()) for _ in range(n)]
# last = stack[-1]
# count = 1

# for i in reversed(range(n)):
#     if stack[i] > last:
#         count += 1
#         last = stack[i]

# print(count)