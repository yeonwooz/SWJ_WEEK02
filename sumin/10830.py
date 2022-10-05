import sys

n, b = map(int, sys.stdin.readline().split())

arr = []
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    arr.append(a)

def colrow_multi(arr1, arr2):
    temp = [[0] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += arr1[row][i] * arr2[i][col]
            temp[row][col] = e % 1000
    return temp

def col_row(arr, r):
    if r == 1:
        for i in range(len(arr)):
            for j in range(len(arr)):
                arr[i][j] %= 1000
        return arr

    else:
        cr = col_row(arr, r // 2)
        m = colrow_multi(cr, cr)
        if r % 2 == 0:
            return m
        else:
            return colrow_multi(m, arr)

new_arr = col_row(arr, b)

for i in new_arr:
    for j in i:
        print(j, end = ' ')
    print()
