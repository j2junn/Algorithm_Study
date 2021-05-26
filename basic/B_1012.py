import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 2

    while queue:
        cx, cy = queue.popleft()
        # graph[cx][cy] = 0

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M or graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1 and graph[nx][ny] != 2:
                queue.append((nx, ny))
                graph[cx][cy] = 2
            


T = int(sys.stdin.readline())

answer = [0 for _ in range(T)]

for t in range(T):

    # M: 가로길이
    # N: 세로길이
    # K: 배추가 심어져 있는 위치의 개수
    M, N, K = map(int, sys.stdin.readline().split())

    graph = [[0 for _ in range(M)] for _ in range(N)]

    # print(graph)

    for _ in range(K):

        x, y = map(int, sys.stdin.readline().split())

        graph[x][y] = 1

    print(graph)

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                BFS(i, j)
                answer[t] += 1
    
print(answer)
