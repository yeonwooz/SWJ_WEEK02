import sys

m, n, l = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

animal = []
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    animal.append(a)

arr.sort()

catched = 0

for i in range(n):
    start = 0
    end = m - 1
    while start <= end:
        mid = (start + end) // 2
        shoot_range = arr[mid]

        if animal[i][1] > l:
            break

        if abs(animal[i][0] - shoot_range) + animal[i][1] <= l:
            catched += 1
            break

        elif animal[i][0] < shoot_range:
            end = mid - 1
        elif animal[i][0] > shoot_range:
            start = mid + 1

print(catched)
