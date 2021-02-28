import sys
from collections import deque

def BFS(x, y):
    cnt_house = 1

    queue.append((x, y))
    maps[x][y] = 2

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N or maps[nx][ny] == 0 or maps[nx][ny] == 2:
                continue

            if maps[nx][ny] == 1:
                queue.append((nx, ny))
                maps[nx][ny] = 2

                cnt_house += 1

    return cnt_house

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(sys.stdin.readline())

maps = []
for _ in range(N):
    maps.append(list(map(int, sys.stdin.readline().strip())))

cnt_danji = 0

queue = deque()

cnt_house = []

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            cnt_house.append(BFS(i, j))
            cnt_danji += 1

print(cnt_danji)
for cnt in sorted(cnt_house):
    print(cnt)

