# 제로 10773
import sys
input = sys.stdin.readline
n = int(input())
result = []
for i in range(n):
    a = int(input())
    if a != 0:
        result.append(a)
    else:
        result.pop()

print(sum(result))