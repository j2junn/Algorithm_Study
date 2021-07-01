# 쉬운 문제이지만 row, col을 헷갈릴 수 있는 점 주의하자
import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(r, c):
    queue = deque()
    queue.append((r, c))
    graph[r][c] = 0

    while queue:
        c_row, c_col = queue.popleft()
        
        for i in range(4):
            n_row = dr[i] + c_row
            n_col = dc[i] + c_col
            
            if n_row < 0 or n_row >= N or n_col < 0 or n_col >= M or graph[n_row][n_col] == 0:
                continue
            
            if graph[n_row][n_col] == 1:
                queue.append((n_row, n_col))
                graph[n_row][n_col] = 0
            
answer = []
T = int(sys.stdin.readline())

for _ in range(T):
    # M: col
    # N: row
    M, N, K = map(int, sys.stdin.readline().split())
    
    graph = [[0 for _ in range(M)] for _ in range(N)]
        
    for _ in range(K):
        # X: col
        # Y: row
        X, Y = map(int, sys.stdin.readline().split())
        
        graph[Y][X] = 1
        
    ans = 0
       
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                BFS(i, j)
                ans += 1
    
    answer.append(ans)

for a in answer:
    print(a)