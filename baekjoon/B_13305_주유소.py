import sys

answer = 0

N = int(sys.stdin.readline())
edges = list(map(int, sys.stdin.readline().split()))
nodes = list(map(int, sys.stdin.readline().split()))

cost = nodes[0]
for i in range(N - 1):
    if cost > nodes[i]:
        cost = nodes[i]
    answer += cost * edges[i]

print(answer)