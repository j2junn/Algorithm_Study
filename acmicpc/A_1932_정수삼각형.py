# 삼각형의 맨 아래층부터 위로 올라가면서 i, i+1 인덱스의 max값을 바로 위층에 더해주는 방식으로 풀었다.
# 단순히 위에서 아래로 내려가면서 max값을 더해주는 방법은 옳지않다. why? 중간에 아주 큰 숫자가 있을 수 도 있는데 고려 x
import sys

n = int(sys.stdin.readline())

graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    
for i in range(n - 1, 0, -1):
    for j in range(len(graph[i]) - 1):
        graph[i - 1][j] += max(graph[i][j], graph[i][j + 1])

print(graph[0][0])