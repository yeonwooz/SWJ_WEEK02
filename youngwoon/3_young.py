# 공유기 설치 2110
import sys
N, C = map(int, input().split())
input = sys.stdin.readline
house = [int(input()) for _ in range(N)]
house.sort()
start = 1
end = house[-1]- house[0]
result = 0

while start <= end:
    mid = (start + end)//2
    count = 1
    old = 0
    for i in range(1, len(house)):
        if house[i]-house[old] >= mid:
            old = i
            count += 1
    
    if count < C:
        end = mid - 1
    else:
        start = mid +1
        result = mid
print(result)