# 괄호 9012
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    a = input().split()[0]
    sum = 0
    if len(a) % 2 == 0:
        for i in a:
            if i == '(':
                sum += 1
            elif i == ')':
                sum -= 1
            if sum < 0:
                break
        if sum == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')