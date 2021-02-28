import sys

flag = False

def DFS(graph, start, visited, b, count):
    global flag
    
    if start == b:
        flag = True
        return count

    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            ret = DFS(graph, i, visited, b, count + 1)
            if flag:
                return ret

n = int(sys.stdin.readline())

a, b = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)


visited = [False for _ in range(n+1)]

answer = DFS(graph, a, visited, b, 0)

if answer == None:
    answer = -1

print(answer)