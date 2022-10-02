# 사냥꾼 8983
import sys
input = sys.stdin.readline
m, n, l =map(int, input().split())
sade = list(map(int, input().split()))
ani = []
sade.sort()

for _ in range(n):
    p = list(map(int, input().split()))
    ani.append(p)

count = 0
for a,b in ani:
    start, end = 0, len(sade)-1
    mid = 0
    while start < end:
        mid = (start + end)//2
        # 왜 start가 소총수 위치 인덱스인가?
        if sade[mid] < a:
            start = mid+1
        elif sade[mid] > a:
            end = mid-1
        else:
            start = mid
            break
        
    if abs(sade[start] - a) + b <= l:
        count += 1
    elif start+1 < len(sade) and abs(sade[start+1] - a) + b <= l:
        count += 1
    elif start > 0 and abs(sade[start-1] - a) + b <= l:
        count += 1

print(count)