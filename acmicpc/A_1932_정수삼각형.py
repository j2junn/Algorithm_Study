# DP테이블 만들고 푸는법
import sys

# 점화식
# D(n - 1, idx) = max(D(n, idx), D(n, idx + 1)) + Cost(n - 1, idx)

n = int(sys.stdin.readline())
dp = [[0 for _ in range(i + 1)] for i in range(n)]

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
 
dp[n - 1] = graph[n - 1]  
for i in range(n - 2, -1, -1):
    for j in range(len(dp[i])):
        dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]) + graph[i][j]

print(dp[0][0])

# DP테이블 안만들고 푸는법
# 삼각형의 맨 아래층부터 위로 올라가면서 i, i+1 인덱스의 max값을 바로 위층에 더해주는 방식으로 풀었다.
# 단순히 위에서 아래로 내려가면서 max값을 더해주는 방법은 옳지않다. why? 중간에 아주 큰 숫자가 있을 수 도 있는데 고려 x
# import sys

# n = int(sys.stdin.readline())

# graph = []

# for i in range(n):
#     graph.append(list(map(int, sys.stdin.readline().split())))
    
# for i in range(n - 1, 0, -1):
#     for j in range(len(graph[i]) - 1):
#         graph[i - 1][j] += max(graph[i][j], graph[i][j + 1])

# print(graph[0][0])