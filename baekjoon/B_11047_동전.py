import sys

answer = 0

N, K = map(int, sys.stdin.readline().split())

A = []

for _ in range(N):
    A.append(int(sys.stdin.readline()))

for i in range(N - 1, -1, -1):
    if K == 0:
        break
    cnt, K = divmod(K, A[i])
    answer += cnt

print(answer)