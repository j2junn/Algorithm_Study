import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# n: row
# m: col
n, m = map(int, sys.stdin.readline().split())

miro = []

for _ in range(n):
    miro.append(list(map(int, sys.stdin.readline().strip())))

queue = deque()
queue.append((0, 0))

while queue:
    cx, cy = queue.popleft()

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if miro[nx][ny] == 1:
            queue.append((nx, ny))
            miro[nx][ny] = miro[cx][cy] + 1

print(miro[n - 1][m - 1]) 