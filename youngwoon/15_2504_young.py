# 괄호의 값 2504
import sys
input = sys.stdin.readline
a = list(input().strip())
stack = []
tmp = 1
answer = 0
for i in range(len(a)):
    if a[i] == '(':
        stack.append(a[i])
        tmp *= 2

    elif a[i] == '[':
        stack.append(a[i])
        tmp *= 3

    elif a[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if a[i-1] == '(':
            answer += tmp
        stack.pop()
        tmp //=2

    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if a[i-1] == '[':
            answer += tmp
        
        stack.pop()
        tmp //=3

if stack:
    print(0)
else:
    print(answer)