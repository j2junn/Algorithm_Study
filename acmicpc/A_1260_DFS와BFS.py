import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

# 문제의 입력은 1부터 시작해서 가독성 위해 N+1 개의 graph, visited 리스트 생성
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for i in range(M):
    # 두 개의 정점을 입력 받는다
    node1, node2 = map(int, sys.stdin.readline().split())
    
    # 간선은 양방향이므로 반대로도 저장
    graph[node1].append(node2)
    graph[node2].append(node1)
    
def DFS(v):
    visited[v] = True
    print(v, end=" ")
    
    # 정점 번호가 작은 것을 먼저 방문해야하므로 sorted 사용
    for i in sorted(graph[v]):
        if not visited[i]:
            DFS(i)
            
def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    
    while queue:
        cv = queue.popleft()
        print(cv, end=" ")
        
        # 정점 번호가 작은 것을 먼저 방문해야하므로 sorted 사용
        for i in sorted(graph[cv]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True    
            
DFS(V)
visited = [False for _ in range(N + 1)]
print("")
BFS(V)