import sys

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    arr.append(a)

white_count = 0
blue_count = 0
def color_paper(x, y, n):
    global white_count
    global blue_count

    color = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != arr[i][j]:
                color_paper(x, y, n // 2)
                color_paper(x, y + n // 2, n // 2)
                color_paper(x + n // 2, y, n // 2)
                color_paper(x + n // 2, y + n // 2, n // 2)
                return

    if color == 0:
        white_count += 1
    else:
        blue_count += 1

    return
color_paper(0, 0, n)
print(white_count)
print(blue_count)

