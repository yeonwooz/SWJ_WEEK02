import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr = sorted(arr)

pl = 0
pr = n - 1
answer = abs(arr[pl] + arr[pr])
final = (arr[pl], arr[pr])

while pl < pr:
    sum = arr[pl] + arr[pr]

    if answer > abs(sum):
        answer = abs(sum)
        final = (arr[pl], arr[pr])
        if answer == 0:
            break

    elif sum < 0:
        pl += 1
    else:
        pr -= 1

print(final[0], final[1])
