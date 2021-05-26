import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []

# N: row
# M: col
N, M = map(int, sys.stdin.readline().split())

visited = [[[0] * 2  for _ in range(M)] for _ in range(N)]

for _ in range(N):
    layer = list(map(int, sys.stdin.readline().strip()))
    graph.append(layer)
# print(graph)


def BFS():
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = 1

    while queue:
        cx, cy, wall = queue.popleft()
        if cx == N - 1 and cy == M - 1:
            return visited[cx][cy][wall]
            

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            # if cx == 0 and cy == 0 and graph[0][1] == 1 and graph[1][0] == 1:
            #     flag -= 1

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny][wall] == 0:
                if graph[nx][ny] == 0:
                    queue.append((nx, ny, wall))
                    visited[nx][ny][wall] = visited[cx][cy][wall] + 1

                if wall == 0 and graph[nx][ny] == 1:
                    queue.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[cx][cy][wall] + 1

    return -1

print(BFS())