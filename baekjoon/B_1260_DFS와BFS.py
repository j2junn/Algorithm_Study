import sys
from collections import deque

def DFS(v):
    visited[v] = True

    print(v, end=" ")

    for g in sorted(graph[v]):
        if not visited[g]:
            DFS(g)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        cv = queue.popleft()

        print(cv, end=" ")

        for g in sorted(graph[cv]):
            if not visited[g]:
                queue.append(g)
                visited[g] = True


# 정점의 개수 N(1 ≤ N ≤ 1,000), 
# 간선의 개수 M(1 ≤ M ≤ 10,000), 
# 탐색을 시작할 정점의 번호 V

N, M, V = map(int, sys.stdin.readline().split())

visited = [False for _ in range(N + 1)]

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())

    graph[v1].append(v2)
    graph[v2].append(v1)


DFS(V)

visited = [False for _ in range(N + 1)]

print("")
BFS(V)
