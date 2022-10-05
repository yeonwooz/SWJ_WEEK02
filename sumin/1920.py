import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
compare_arr = list(map(int, sys.stdin.readline().split()))

arr = sorted(arr)


def binary_search(num):
    pl = 0
    pr = len(arr) - 1
    pc = len(arr) // 2

    while True:
        if pl > pr:
            return 0

        if num < arr[pc]:
            pr = pc - 1
            pc = (pl + pr) // 2
        elif num == arr[pc]:
            return 1
        elif num > arr[pc]:
            pl = pc + 1
            pc = (pl + pr) // 2


for i in compare_arr:
    print(binary_search(i))
