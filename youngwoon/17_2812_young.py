# 크게 만들기 2812

n, k = map(int, input().split())
nums = input()
stack = []
del_count = k

for i in range(n):
    while del_count > 0 and stack:
        if nums[i] > stack[-1]:
            stack.pop()
            del_count -= 1
        else:
            break
    stack.append(nums[i])

result = ''
for i in range(n-k):
    result += stack[i]
print(result)