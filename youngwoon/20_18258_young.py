# 큐2 18258
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
queue = deque()

for i in range(n):
    a = list(input().split())

    if a[0] == 'push':
        queue.append(a[1])

    elif a[0] == 'pop':
        if queue:
            print(queue[0])
            queue.popleft()
        else:
            print(-1)

    elif a[0] == 'size':
        print(len(queue))

    elif a[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif a[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif a[0] == 'back':
        if queue:
            print(queue[len(queue)-1])
        else:
            print(-1)