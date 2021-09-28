answer = 4
N, M, H = map(int, input().split())

ladder = [[0 for _ in range(N)] for _ in range(H)]

for _ in range(M):
    r, c = map(int, input().split())
    ladder[r - 1][c - 1] = 1

    
# 각 col마다 아래로 내려가면서 자기 자신의 col로 내려가는지 검사
def check():
    for i in range(N):
        now = i
        for j in range(H):
            # now가 1이면 (now, now+1)이 연결되어 있으므로, 오른쪽으로 이동(now += 1)
            if ladder[j][now] == 1:
                now += 1
            # (now - 1)이 1이면 (now-1, now)가 연결되어 있으므로, 왼쪽으로 이동(now -= 1)
            elif ladder[j][now - 1] == 1:
                now -= 1
        if now != i:
            return False
    return True


def solve(cnt, x, y):
    global answer
    
    if answer <= cnt:
        return
    if check():
        answer = min(answer, cnt)
        return
    if cnt == 3:
        return 

    for i in range(x, H):
        if x == i:
            k = y
        else:
            k = 0
        
        for j in range(k, N - 1):
            if ladder[i][j] == 1:
                j += 1
            else:
                ladder[i][j] = 1
                solve(cnt + 1, i, j + 2)
                ladder[i][j] = 0

solve(0, 0, 0)
print(answer if answer < 4 else -1)