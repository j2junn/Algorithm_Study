import sys

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


x, y = map(int, sys.stdin.readline().split())

g = gcd(x, y)

print(g)
print((x * y) // g)

