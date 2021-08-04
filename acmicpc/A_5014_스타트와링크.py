from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [False for _ in range(F + 1)]
visited[0] = True

visited[S] = True

q = deque()
q.append((S, 0))

while q:
    now, cnt = q.popleft()
    
    if now == G:
        print(cnt)
        exit()
        
    for i in [U, -D]:
        next = now + i
        
        if next <= 0 or next > F:
            continue
        
        if not visited[next]:
            visited[next] = True
            q.append((next, cnt + 1))

print("use the stairs")