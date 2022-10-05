import sys

n, k = map(int, sys.stdin.readline().split())

arr = []
for i in range(n):
    a = int(sys.stdin.readline())
    arr.append(a)

arr.sort()

start = arr[0]
end = arr[n - 1] + k

max_level = 0

while start <= end:
    mid = (start + end) // 2

    count = 0
    for i in arr:
        if i < mid:
            count += (mid - i)

    if count <= k:
        max_level = mid
        start = mid + 1
    else:
        end = mid - 1

print(max_level)
