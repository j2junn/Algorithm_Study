import sys
from collections import deque

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = []

N = int(sys.stdin.readline())
graph = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))


def BFS(r, c, cnt):
    queue = deque()
    queue.append((r, c))
    graph[r][c] = 0

    
    while queue:
        c_row, c_col = queue.popleft()
        
        # 상 하 좌 우 하나씩 이동하면서        
        for i in range(4):
            n_row = c_row + dr[i]
            n_col = c_col + dc[i]

            # 이동하려는 좌표가 graph 밖이거나 벽(0)이면 제외하고
            if n_row < 0 or n_row >= N or n_col < 0 or n_col >= N or graph[n_row][n_col] == 0:
                continue
            
            # 벽(0)이 아니면 큐에 데이터 쌓고 벽으로 만든 후 카운팅+1
            if graph[n_row][n_col] == 1:
                queue.append((n_row, n_col))
                graph[n_row][n_col] = 0
                cnt += 1
    
    return cnt
        

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            ans.append(BFS(i, j, 1))
           
                
print(len(ans))
for a in sorted(ans):
    print(a)