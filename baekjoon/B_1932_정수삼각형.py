import sys

answer = 0

tc = int(sys.stdin.readline())

graph = []

for i in range(tc):
    layer = list(map(int, sys.stdin.readline().split()))
    graph.append(layer)

for i in range(tc - 1, 0, -1):
    for j in range(0, len(graph[i]) - 1):
        # print(max(graph[i][j], graph[i][j + 1]))
        graph[i - 1][j] += max(graph[i][j], graph[i][j + 1])
        
print(graph[0][0])
