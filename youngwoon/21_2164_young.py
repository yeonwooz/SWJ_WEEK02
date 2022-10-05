# 카드2 2164
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
q = deque([i for i in range(1, n+1)])   # 범위 조심

while len(q) > 1:
    q.popleft()
    num = q.popleft()
    q.append(num)

print(q[0])