# 오른쪽, 아래
dr = [0, 1]
dc = [1, 0]

def solution(m, n, puddles):
    # n: row
    # m: col
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
            
    for r in range(n):
        for c in range(m):
            if r == c == 0:
                continue
            if [c + 1, r + 1] in puddles:
                dp[r][c] = 0
            else:
                dp[r][c] = (dp[r - 1][c] + dp[r][c - 1]) % 1000000007
    

    return dp[n - 1][m - 1]