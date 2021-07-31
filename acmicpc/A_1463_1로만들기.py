N = int(input())

# 입력값이 3 이하인 경우를 위해 N+3으로 설정(최소한의 메모리)
dp = [0 for _ in range(N + 3)]

dp[1] = 0
dp[2] = 1
dp[3] = 1

if N > 4:
    for i in range(4, N + 1):
        if i % 3 == 0 and i % 2 == 0:
            dp[i] = min(dp[i // 3], dp[i // 2], dp[i - 1]) + 1  
        elif i % 3 == 0:
            dp[i] = min(dp[i // 3], dp[i - 1]) + 1
        elif i % 2 == 0:
            dp[i] = min(dp[i // 2], dp[i - 1]) + 1
        else:
            dp[i] = dp[i - 1] + 1

print(dp[N])