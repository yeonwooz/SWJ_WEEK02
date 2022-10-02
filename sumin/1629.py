import sys

a, b, c = map(int, sys.stdin.readline().split())

def multi(num, r):
    if r == 1:
        return (num % c)

    else:
        m = multi(num, r // 2)
        if r % 2 == 0:
            return (m * m) % c

        else:
            return (m * m * num) % c

print(multi(a, b))
