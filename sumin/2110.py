import sys

n, c = map(int, sys.stdin.readline().split())

arr = []
for i in range(n):
    a = int(sys.stdin.readline())
    arr.append(a)

home = sorted(arr)

start = 1
end = home[- 1] - home[0]

length = 0

while start <= end:
    mid = (start + end) // 2
    wifi = home[0]
    count = 1

    for i in range(len(home)):
        if home[i] >= wifi + mid:
            count += 1
            wifi = home[i]

    if count >= c:
        length = mid
        start = mid + 1

    else:
        end = mid - 1

print(length)
