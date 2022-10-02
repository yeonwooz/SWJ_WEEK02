# 가장 가까운 두 점 2261
# mid는 행의 중앙값을 탐색한 값인데 왜 x축 최소거리를 찾는데 쓰이는지?

n = int(input())

num_list = [[list(map(int, input().split()))] for _ in range(4)]

def measure(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def find(start, end):
    if start == end:
        return float('inf')
    if end - start == 1:
        return measure(num_list[start], num_list[end])
    
    # 분할정복
    mid = (start + end)//2
    min_dist = min(find(start, mid), find(mid, end))

    # x축 최소거리 비교
    min_list = []
    for i in range(start, end+1):
        if num_list[mid][0] - num_list[i][0] < min_dist:
            min_list.append(num_list[mid][0] - num_list[i][0])

    # y축 최소거리 비교
    min_list.sort()
    for 




print(find(0, n-1))