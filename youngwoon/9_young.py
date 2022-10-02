# 행렬 제곱 10830

n, b = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

def mat(n, b, arr):
    if b == 1:
        return arr
    elif b ==2:
        return mul(n, arr, arr)
    else:
        result = mat(n, b//2, arr)
        if b%2 == 0:
            return mul(n, result, result)
        else:
            return mul(n, mul(n , result, result), arr)

def mul(n, arr1, arr2):
    a = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                a[i][j] += arr1[i][k] * arr2[k][j]
            a[i][j] %= 1000
    return a

answer = mat(n, b, arr)
for i in answer:
    for j in i:
        print(j % 1000, end=' ')
    print()