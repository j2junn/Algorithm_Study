import sys
import math

answer = 0

N = int(sys.stdin.readline())

for i in range(1, N + 1):
    answer += i * (N // i)

print(answer)