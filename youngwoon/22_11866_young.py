# 요세푸스 문제 11866
import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

q = deque([i for i in range(1, n+1)])
answer = []

while len(q) > 0:
    for i in range(k-1):
        q.append(q.popleft())
    answer.append(q.popleft())

# for j in answer:
print(f'<{", ".join(map(str, answer))}>' )