# 스택 10828
import sys
n = int(input())

stack = []
answer = []
for _ in range(n):
    input = sys.stdin.readline
    commend = list(input().split())
    
    if commend[0] == 'push':
        stack.append(commend[1])
    
    elif commend[0] == 'pop':
        if len(stack) != 0:
            answer.append(stack[-1])
            stack.pop()
        else:
            answer.append(-1)

    elif commend[0] == 'size':
        answer.append(len(stack))

    elif commend[0] == 'empty':
        if len(stack) == 0:
            answer.append(1)
        else:
            answer.append(0)
    
    elif commend[0] == 'top':
        if len(stack) != 0:
            answer.append(stack[len(stack)-1])
        else:
            answer.append(-1)

for i in range(len(answer)):
    print(answer[i])