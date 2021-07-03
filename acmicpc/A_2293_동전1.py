import sys

coins = []

n, k = map(int, sys.stdin.readline().split())
dp = [0 for _ in range(k + 1)]
dp[0] = 1

for _ in range(n):
    coins.append(int(sys.stdin.readline()))
    
# dp[1]은 1원을 만들 수 있는 경우의 수
# dp[i] += dp[i - 동전 종류]
# 동전 하나씩 경우를 그려보면서 점화식을 구하자
for c in coins:
    for i in range(1, k + 1):
        if i >= c:
            dp[i] += dp[i - c]
        
print(dp[k])
