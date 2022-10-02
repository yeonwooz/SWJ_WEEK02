# 두용액 2470
N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

left = 0
right = N-1
result = [liquid[left], liquid[right]]
comp = abs(liquid[left] + liquid[right])


while left < right:
    sum = liquid[left] + liquid[right]
    if abs(sum) < comp:
        comp = abs(sum)
        result = [liquid[left], liquid[right]]
        if abs(sum) ==0:
            break
    if sum > 0:
        right -= 1
    else:
        left += 1

print(result[0], result[1])