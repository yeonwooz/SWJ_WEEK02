# 곱셈 1629

A, B, C = map(int, input().split())

def mod(a, b):
    global C
    if b ==1:
        return a%C
    else:
        result = mod(a, b//2)
        if b%2 ==0:
            return (result * result)%C
        else:
            return (result * result * a)%C

print(mod(A, B))