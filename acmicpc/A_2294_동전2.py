n, k = map(int, input().split())
coins = []
dp = [0 for _ in range(k + 1)]

for _ in range(n):
    coins.append(int(input()))
    
for i in range(1, k + 1):
    comp = []
    
    for coin in coins:
        if i >= coin and dp[i - coin] != -1:
            comp.append(dp[i - coin])
        
    if not comp:
        dp[i] = -1
    else:
        dp[i] = min(comp) + 1
    
print(dp[k])