# 수 찾기 1920
from sys import stdin

n = stdin.readline()
or_list = list(map(int, input().split()))
or_list.sort()
n_2 = int(stdin.readline())
serch_list = list(map(int, input().split()))
serch_list.sort()

def serch(m ,or_list, start, end):
    if start > end:
        return 0
    pc = (end + start)//2
    if m == or_list[pc]:
        return 1
    elif m < or_list[pc]:
        return serch(m ,or_list, start, pc-1)
    else:
        return serch(m ,or_list, pc+1, end)
    
for i in serch_list:
    start = 0
    end = len(or_list)-1
    print(serch(i ,or_list, start, end))

# result = [0] * n_2
# for i in range(len(serch_list)):
#     for j in range(c):
#         if or_list[j] == serch_list[i]:
#             result[i] += 1

# for k in result:
#     print(k)