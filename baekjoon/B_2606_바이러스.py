import sys
from collections import deque

n = int(sys.stdin.readline())

m = int(sys.stdin.readline())

visited = [False for _ in range(n)]

graph = [[] for _ in range(n)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x - 1].append(y - 1)
    graph[y - 1].append(x - 1)

cnt = 0

queue = deque()
queue.append(0)
visited[0] = True

while queue:
    c = queue.popleft()

    for g in graph[c]:
        if not visited[g]:
            queue.append(g)
            visited[g] = True
            cnt += 1

print(cnt)