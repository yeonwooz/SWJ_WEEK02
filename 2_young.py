# 나무 자르기 2805
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()

start = 1
end = max(tree)
length = 0
while start <= end:
    mid = (start + end)//2

    get = 0
    for i in tree:
        if i >= mid:
            get += i - mid

    if get >= M:
        start = mid + 1
        length = mid
    else:
        end = mid - 1
        

print(length)
