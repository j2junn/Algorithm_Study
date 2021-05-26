import sys
from collections import deque

# N: 정점의 개수
# M: 간선의 개수
# V: 정점의 번호
N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
# print(graph)

for i in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    
    graph[n1].append(n2)
    graph[n2].append(n1)


def DFS(V):
    visited[V] = True

    print(V, end=" ")

    for g in sorted(graph[V]):
        if not visited[g]:
            DFS(g)

def BFS(V):
    queue = deque()
    queue.append(V)
    visited[V] = True

    while queue:
        CV = queue.popleft()
        print(CV, end=" ")

        for g in sorted(graph[CV]):
            if not visited[g]:
                queue.append(g)
                visited[g] = True
                

DFS(V)
visited = [False for _ in range(N + 1)]
print("")
BFS(V)