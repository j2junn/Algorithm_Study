import itertools
answer = float('inf')

def calc_distance(d1, d2):
    return abs(d1[0] - d2[0]) + abs(d1[1] - d2[1])


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

# city에서 집, 치킨집 좌표만 찾아서 따로 저장
homes = []
chickens = []

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            homes.append((r, c))
        elif city[r][c] == 2:
            chickens.append((r, c))
            
# 치킨집중에 M개를 선택하는 경우들
cases = list(itertools.combinations(chickens, M))

# 경우들 한개씩 돌면서 거리 합을 min을 answer에 담기
for case in cases:
    
    # 각 집마다 가장 가까운 치킨집과의 치킨거리가 저장됨
    home = [float('inf') for _ in range(len(homes))]
    
    # 케이스의 한 경우(한 치킨집과 여러개의 집들 사이의 치킨거리)
    for c in case:
        for i in range(len(homes)):
            home[i] = min(home[i], calc_distance(c, homes[i]))
    
    answer = min(answer, sum(home))

print(answer)