import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# m: col
# n: row 
m, n = map(int, sys.stdin.readline().split())

box = []

for _ in range(n):
    box.append(list(map(int, sys.stdin.readline().split())))

queue = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j))

while queue:
    cx, cy = queue.popleft()

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m or box[nx][ny] == -1:
            continue

        if box[nx][ny] == 0:
            queue.append((nx, ny))
            box[nx][ny] = box[cx][cy] + 1

answer = 0

for b in box:
    if 0 in b:
        answer = -1

if answer != -1:
    answer = max(map(max, box)) - 1

print(answer)