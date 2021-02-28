def DFS(n, computers, v, visited):
    visited[v] = True

    for i in range(n):
        if v != i and computers[v][i] == 1:
            if not visited[i]:
                DFS(n, computers, i, visited)       

def solution(n, computers):
    answer = 0

    visited = [False for _ in range(n)]

    for i in range(n):
        if not visited[i]:
            DFS(n, computers, i, visited)
            answer += 1

    return answer