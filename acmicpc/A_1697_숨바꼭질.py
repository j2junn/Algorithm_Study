import sys
from collections import deque
answer = 0

N, K = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(100001)]

queue = deque()
queue.append(N)

while queue:

    now = queue.popleft()
    
    if now == K:
        print(visited[now]) 
        break
    
    # 이미 방문했던 숫자는 다시 방문하지 않아야 메모리 초과 문제가 일어나지 않음
    for nxt in [now - 1, now + 1, now * 2]:       
        if 0 <= nxt < 100001 and visited[nxt] == 0:
            visited[nxt] = visited[now] + 1
            queue.append(nxt)