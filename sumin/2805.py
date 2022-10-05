import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(tree)

cut_length = 0
while start <= end:
    mid = (start + end) // 2

    mount = 0
    for t in tree:
        if t >= mid:
            mount = mount + (t - mid)

    if mount >= m:
        cut_length = mid
        start = mid + 1

    else:
        end = mid - 1

print(cut_length)
