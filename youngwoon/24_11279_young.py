# 최대 힙 11279
import heapq
import sys

input = sys.stdin.readline
n = int(input())
h = []

for i in range(n):
    a = int(input())    
    if a != 0:
        heapq.heappush(h, -a)

    elif a == 0:
        if h:
            print(-1*heapq.heappop(h))
        else:
            print('0')