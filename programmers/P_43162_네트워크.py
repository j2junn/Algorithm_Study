def DFS(start, computers, visited):
    stack = [start]

    while stack:
        now = stack.pop()

        if not visited[now]:
            visited[now] = True

        for i in range(len(computers)):
            if computers[now][i] == 1 and not visited[i]:
                stack.append(i)

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    i = 0
    while False in visited:
        if not visited[i]:
            DFS(i, computers, visited)
            answer += 1
        i += 1
        
    return answer