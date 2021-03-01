# DFS 로 해결하려했으나 Recursion error 로 인해 BFS로 해결함

# import sys

# def DFS(row, col):
#     bat[row][col] = 2

#     for i in range(4):
#         n_row = row + dx[i]
#         n_col = col + dy[i]

#         if n_row < 0 or n_row >= N or n_col < 0 or n_col >= M or bat[n_row][n_col] == 0:
#             continue
        
#         if bat[n_row][n_col] == 1 and bat[n_row][n_col] != 2:
#             DFS(n_row, n_col)


# # T: 테스트 케이스의 개수
# # M: 가로길이 (col)
# # N: 세로길이 (row)
# # K: 배추가 심어져 있는 위치의 개수

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# T = int(sys.stdin.readline())

# answer = [0 for _ in range(T)]


# for t in range(T):
#     M, N, K = map(int, sys.stdin.readline().split())

#     bat = [[0 for _ in range(M)] for _ in range(N)]


#     for _ in range(K):

#         col, row = map(int, sys.stdin.readline().split())

#         bat[row][col] = 1


#     cnt = 0

#     for i in range(N):
#         for j in range(M):
#             if bat[i][j] == 1:
#                 DFS(i, j)
#                 cnt += 1

#     answer[t] = cnt

# for a in answer:
#     print(a)

import sys
from collections import deque

def BFS(row, col):
    queue = deque()
    queue.append((row, col))
    bat[row][col] = 2

    while queue:
        c_row, c_col = queue.popleft()

        for i in range(4):
            n_row = c_row + dx[i]
            n_col = c_col + dy[i]

            if n_row < 0 or n_row >= N or n_col < 0 or n_col >= M or bat[n_row][n_col] == 0:
                continue
            
            if bat[n_row][n_col] == 1 and bat[n_row][n_col] != 2:
                queue.append((n_row, n_col))
                bat[n_row][n_col] = 2

# T: 테스트 케이스의 개수
# M: 가로길이 (col)
# N: 세로길이 (row)
# K: 배추가 심어져 있는 위치의 개수

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(sys.stdin.readline())

answer = [0 for _ in range(T)]


for t in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    bat = [[0 for _ in range(M)] for _ in range(N)]


    for _ in range(K):

        col, row = map(int, sys.stdin.readline().split())

        bat[row][col] = 1

    cnt = 0

    for i in range(N):
        for j in range(M):
            if bat[i][j] == 1:
                BFS(i, j)
                cnt += 1

    answer[t] = cnt

for a in answer:
    print(a)