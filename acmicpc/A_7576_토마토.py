from collections import deque

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
box = []

col, row = map(int, input().split())

for _ in range(row):
    box.append(list(map(int, input().split()))) 

q = deque()

for r in range(row):
    for c in range(col):
        if box[r][c] == 1:
            q.append((r, c))
            
while q:
    rr, cc = q.popleft()
    
    for i in range(4):
        nr = rr + dr[i]
        nc = cc + dc[i]
        
        if nr < 0 or nr >= row or nc < 0 or nc >= col or box[nr][nc] == -1:
            continue
        
        if box[nr][nc] == 0:
            box[nr][nc] = box[rr][cc] + 1
            q.append((nr, nc))
            

for r in range(row):
    if 0 in box[r]:
        print(-1)
        exit()
        
print(max(map(max, box)) - 1)