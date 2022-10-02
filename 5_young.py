# 히오스 프로게이머 16564
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
X = [int(input()) for _ in range(N)]
X.sort()

start = X[0]
end = X[0] + K

T = 0
while start <= end:
    mid = (start + end)//2
    levels = 0
    for i in X:
        if i < mid:
            levels += (mid - i)

    if levels <= K:
        start = mid + 1
        T = mid
    else:
        end = mid - 1

print(T)
