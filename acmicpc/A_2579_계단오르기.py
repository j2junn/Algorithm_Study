# N: 계단의 수
N = int(input())
stairs = []

for _ in range(N):
    stairs.append(int(input()))

dp = [0 for _ in range(N + 1)]

dp[0] = stairs[0]
if N == 1:
    print(dp[0])
    exit()
    
dp[1] = stairs[0] + stairs[1]
if N == 2:
    print(dp[1])
    exit()

dp[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2])

    
for i in range(3, N):
    dp[i] = max(stairs[i] + stairs[i - 1] + dp[i - 3], stairs[i] + dp[i - 2])

print(dp[N - 1])