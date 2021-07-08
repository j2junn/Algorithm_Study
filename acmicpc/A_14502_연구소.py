import sys
from collections import deque
from itertools import permutations, combinations

# 리스트를 복사해서 쓰려고 사용함
from copy import deepcopy

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# N(row): 세로 크기
# M(col): 가로 크기
N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))


def findCases():
    cases = []
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cases.append((i, j))
    
    cases = list(combinations(cases, 3))

    return cases


def countZero(g):
    cnt = 0
    
    for i in range(N):
        cnt += g[i].count(0)
    
    return cnt


def checkMax(case, g, v):
    
    # 3개의 벽 세우기
    for c in case:
        g[c[0]][c[1]] = 1
    
    q = deque()

    for i in range(N):
        for j in range(M):
            if g[i][j] == 2:
                q.append((i, j))
                
    while q:
        now_r, now_c = q.popleft()
        v[now_r][now_c] = True
        
        for i in range(4):
            nxt_r = now_r + dr[i]
            nxt_c = now_c + dc[i]

            if nxt_r < 0 or nxt_r >= N or nxt_c < 0 or nxt_c >= M or g[nxt_r][nxt_c] == 1 or g[nxt_r][nxt_c] == 2:
                continue
            
            if g[nxt_r][nxt_c] == 0 and not v[nxt_r][nxt_c]:
                q.append((nxt_r, nxt_c))
                v[nxt_r][nxt_c] = True
                g[nxt_r][nxt_c] = 1
    
    cnt = countZero(g)
    return cnt
    

answer = []

# 1. 3개의 벽을 세울 수 있는 경우 구하기
cases = findCases()

# 2. 각 케이스마다 BFS돌려서 안전영역 최대 크기를 구하기
for case in cases:
    visited = [[False for _ in range(M)] for _ in range(N)]
    # graph를 계속 변형시키면서 0의 개수를 구할꺼라서 새로운 g 라는 graph로 deepcopy한다
    g = deepcopy(graph)
    cnt = checkMax(case, g, visited)
    answer.append(cnt)

print(max(answer))