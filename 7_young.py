# 색종이 만들기 2630
import sys

input = sys.stdin.readline
n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]
# result = []
white = 0
blue = 0

def divide(x, y, n):
    global white, blue
    color = paper[x][y]
    # 나누어진 전체 종이의 색깔이 같은지 확인
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != color:
                divide(x, y, n//2)
                divide(x, y+n//2, n//2)
                divide(x+n//2, y, n//2)
                divide(x+n//2, y+ n//2, n//2)
                return
    # 색깔이 다 같으면 result에 추가
    if color == 0:
        white += 1
    else:
        blue += 1

# 종이가 1칸일 경우와 2칸 이상일 경우
if n == 1:
    if paper[0][0] == 0:
        white += 1
    else:
        blue += 1
else:
    divide(0, 0, n)

print(white)
print(blue)