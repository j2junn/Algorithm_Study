import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

visited = [False for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    
    graph[node1].append(node2)
    graph[node2].append(node1)
    
    
def BFS(v, ans):
    queue = deque()
    queue.append(v)
    visited[v] = True
    
    while queue:
        cv = queue.popleft()
        
        # 큐에 들어있는 노드를 하나씩 꺼낼 때마다 바이러스에 걸린 것을 확인하게 되므로
        ans += 1
        
        for i in graph[cv]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
    return ans
    
# 시작하는 1번 컴퓨터를 제외한 나머지의 합을 구해야하므로
print(BFS(1, 0) - 1)

