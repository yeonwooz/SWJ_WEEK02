import sys
input = sys.stdin.readline
n = int(input())
or_list = list(map(int, input().split()))
or_list.sort()

n_1 = int(input())
serch_list = list(map(int, input().split()))

for i in serch_list:
    start = 0
    end = n-1
    isExist = False
    while start <= end:
        cen = (start + end)//2
        if i == or_list[cen]:
            isExist = True
            print(1)
            break
        elif i > or_list[cen]:
            start = cen + 1
        else:
            end = cen - 1
    if not isExist:	
        print(0) 