import sys
import math

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    arr.append(a)

arr1 = sorted(arr)

min_value = sys.maxsize
def dis(arr, r):
    global min_value

    if r == 2:
        d = (arr[1][0] - arr[0][0]) ** 2 + (arr[1][1] - arr[0][1]) ** 2
        return d

    else:
        if r % 2 == 0:
            r //= 2
            value = min(dis(arr[:r], r), dis(arr[r:], r), dis(arr[r - 1:r + 1], r))
        else:
            r = math.ceil(r / 2)
            value = min(dis(arr[:r], r), dis(arr[r - 1:], r))

        min_value = min(min_value, value)
    return min_value

print(dis(arr1, n))
