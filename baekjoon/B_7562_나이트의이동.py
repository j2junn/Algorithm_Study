import sys
from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def BFS(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y1))
    board[x1][y1] = 1

    while queue:
        cx, cy = queue.popleft()

        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue

            if board[nx][ny] == 0:
                queue.append((nx, ny))
                board[nx][ny] = board[cx][cy] + 1

tc = int(sys.stdin.readline())

for _ in range(tc):
    l = int(sys.stdin.readline())

    board = [[0 for _ in range(l)] for _ in range(l)]

    # start
    x1, y1 = map(int, sys.stdin.readline().split())    

    # end
    x2, y2 = map(int, sys.stdin.readline().split())
    
    BFS(x1, y1, x2, y2)

    print(board[x2][y2] - 1)

