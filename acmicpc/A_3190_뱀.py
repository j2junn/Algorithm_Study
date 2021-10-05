import sys
from collections import deque
# 1. 왼쪽위에서 시작 (맨처음엔 오른쪽으로 이동)
# 2. 사과먹으면 꼬리 증가
# 3. 사과없으면 그대로
# 4. 벽이나 자기자신과 부닺히면 게임 끝

# right, down, left, up
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

cnt = 0

# 보드의 크기
N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]

# 사과의 개수
K = int(input())
# 사과의 위치
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1

transform_info = []
# 뱀의 방향 변환 횟수
L = int(input())
# 뱀의 방향 변환 정보
for _ in range(L):
    # X초가 끝난 뒤에 C방향으로 90도 방향 회전
    X, C = input().split()
    X = int(X)
    
    transform_info.append([X, C])

for i in range(L-1, 0, -1):
    transform_info[i][0] -= transform_info[i - 1][0]

board[0][0] = 2


q = deque()
q.append((0, 0))


def DFS(row, col, now_dir, new_dir):
    global cnt, q
    cnt += 1
    
    # 방향 정보 끝나면 종료
    # if new_dir == L:
    #     return
    new_row = row + dr[now_dir]
    new_col = col + dc[now_dir]
 
    # 벽이나 뱀 자기자신을 부딪히면 종료
    if new_row < 0 or new_row >= N or new_col < 0 or new_col >= N:
        return
    
    # 사과 없으면
    if board[new_row][new_col] == 0:
        # 새로운 머리자리는 체크하고 꼬리자리는 비우기
        qr, qc = q.popleft()
        board[qr][qc] = 0
        
    # elif board[new_row][new_col] == 1:
        # 사과 있던 자리(새로운 머리자리)는 체크하고 꼬리자리도 채우기
        
        # board[row][col] = 2
    
    if board[new_row][new_col] == 2:
        return
    
    board[new_row][new_col] = 2
    
    if new_dir < L:
        transform_info[new_dir][0] -= 1
    q.append((new_row, new_col))
    
    # sec 후에 new_dir로 방향 변경
    if new_dir < L and transform_info[new_dir][0] == 0:
        if transform_info[new_dir][1] == 'D':
            now_dir += 1
        elif transform_info[new_dir][1] == 'L':
            now_dir -= 1
        
        # 방향 최대/최소 idx 넘어가는 것 방지
        now_dir %= 4
                
        # 다음 방향을 위해
        new_dir += 1
    
    
    DFS(new_row, new_col, now_dir, new_dir)

sys.setrecursionlimit(10000)
DFS(0, 0, 0, 0)

print(cnt)