import sys
sys.setrecursionlimit(10000)

cnt = 0

# N: 정점의 개수
# M: 간선의 개수
N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())

    graph[u].append(v)
    graph[v].append(u)


def DFS(v):
    visited[v] = True

    for g in graph[v]:
        if not visited[g]:
            DFS(g)
            
        
for i in range(1, N + 1):
    if not visited[i]:
        cnt += 1
        DFS(i)

print(cnt)
