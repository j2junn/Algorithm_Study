import sys

# 점화식
# D(Red, n) = Min(D(Blue, n - 1), D(Green, n - 1)) + Cost(Red, n)
# D(Blue, n) = Min(D(Red, n - 1), D(Green, n - 1)) + Cost(Blue, n)
# D(Green, n) = Min(D(Red, n - 1), D(Blue, n - 1)) + Cost(Green, n)

N = int(sys.stdin.readline())
dp = [[0, 0, 0] for _ in range(N)]
graph = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
    
# 첫 번째 집부터 (N - 1)번째 집까지 이전 집의 DP테이블 이용해서 DP테이블 생성
for i in range(N):
    if i == 0:
        dp[0] = graph[0]
    else:
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + graph[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + graph[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + graph[i][2]

print(min(dp[N - 1]))