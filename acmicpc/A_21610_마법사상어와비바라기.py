# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

answer = 0
N, M = map(int, input().split())

sky = [list(map(int, input().split())) for _ in range(N)]
    
# 구름 위치: 처음 구름 위치 저장
clouds = [[N - 2, 0], [N - 2, 1], [N - 1, 0], [N - 1, 1]]

for _ in range(M):
    d, s = map(int, input().split())
    
    # 1. 모든 구름이 di 방향으로 si칸 이동한다.
    # sky 밖으로 나가면 - 되거나 N 보다 커지는 것을 조정하기 위해 % N을 함
    for cloud in clouds:
        cloud[0] = (cloud[0] + dr[d - 1] * s) % N
        cloud[1] = (cloud[1] + dc[d - 1] * s) % N

        # 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
        sky[cloud[0]][cloud[1]] += 1
        
    # 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 
    # 물복사버그 마법을 사용하면, 
    # 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 
    # (r, c)에 있는 바구니의 물이 양이 증가한다.
    for cloud in clouds:
    
        cnt = 0
        for i in range(1, 8, 2):
            new_row = cloud[0] + dr[i]
            new_col = cloud[1] + dc[i]
            
            # 이 좌표들은 그냥 좌표 자체에서만 대각선 확인 하는 용도이므로 넘어가면 제외     
            if 0 <= new_row < N and 0 <= new_col < N and sky[new_row][new_col] > 0:
                cnt += 1

        sky[cloud[0]][cloud[1]] += cnt
        
    # 3. 구름이 모두 사라진다.
    new_clouds = []
    
    # 이제 구름이 있었던 칸을 제외한 나머지 칸 중에서 물의 양이 2 이상인 칸에 구름이 생긴다. 
    # 구름이 생기면 물의 양이 2만큼 줄어든다.
    for r in range(N):
        for c in range(N):
            # 원래 구름은 포함 x
            if [r, c] not in clouds and sky[r][c] >= 2:
                sky[r][c] -= 2
                new_clouds.append([r, c])
    
    clouds = new_clouds
    

for s in sky:
    answer += sum(s)

print(answer)

# # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
# dr = [0, -1, -1, -1, 0, 1, 1, 1]
# dc = [-1, -1, 0, 1, 1, 1, 0, -1]

# answer = 0
# N, M = map(int, input().split())

# sky = [list(map(int, input().split())) for _ in range(N)]

# def magic(sky, clouds, d, s):
    
#     # 1. 모든 구름이 di 방향으로 si칸 이동한다.
#     # sky 밖으로 나가면 - 되거나 N 보다 커지는 것을 조정하기 위해 % N을 함
#     for cloud in clouds:
#         cloud[0] = (cloud[0] + dr[d - 1] * s) % N
#         cloud[1] = (cloud[1] + dc[d - 1] * s) % N

#         # 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
#         sky[cloud[0]][cloud[1]] += 1
        
#     # 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 
#     # 물복사버그 마법을 사용하면, 
#     # 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 
#     # (r, c)에 있는 바구니의 물이 양이 증가한다.
#     for cloud in clouds:
    
#         cnt = 0
#         for i in range(1, 8, 2):
#             new_row = cloud[0] + dr[i]
#             new_col = cloud[1] + dc[i]
            
#             # 이 좌표들은 그냥 좌표 자체에서만 대각선 확인 하는 용도이므로 넘어가면 제외     
#             if 0 <= new_row < N and 0 <= new_col < N and sky[new_row][new_col] > 0:
#                 cnt += 1

#         sky[cloud[0]][cloud[1]] += cnt
        
#     # 3. 구름이 모두 사라진다.
#     new_clouds = []
    
#     # 이제 구름이 있었던 칸을 제외한 나머지 칸 중에서 물의 양이 2 이상인 칸에 구름이 생긴다. 
#     # 구름이 생기면 물의 양이 2만큼 줄어든다.
#     for r in range(N):
#         for c in range(N):
#             # 원래 구름은 포함 x
#             if [r, c] not in clouds and sky[r][c] >= 2:
#                 sky[r][c] -= 2
#                 new_clouds.append([r, c])
    
#     return sky, new_clouds

# # 구름 위치: 처음 구름 위치 저장
# clouds = [[N - 2, 0], [N - 2, 1], [N - 1, 0], [N - 1, 1]]

# for idx in range(M):
#     d, s = map(int, input().split())
    
#     sky, clouds = magic(sky, clouds, d, s)

# for s in sky:
#     answer += sum(s)

# print(answer)