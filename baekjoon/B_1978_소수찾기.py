import sys

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False

    return True

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

cnt = 0

for num in nums:
    if is_prime(num):
        cnt += 1

print(cnt)