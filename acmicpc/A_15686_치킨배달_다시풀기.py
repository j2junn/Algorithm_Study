import itertools

def calc_street(d1, d2):
    return abs(d1[0] - d2[0]) + abs(d1[1] - d2[1])

# N: row, col
# M: 치킨집 개수

N, M = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]

homes = []
chickens = []

cnt = 0

for r in range(N):
    for c in range(N):
        if maps[r][c] == 1:
            homes.append((r, c))
            cnt += 1
        elif maps[r][c] == 2:
            chickens.append((r, c))
        
mins = 1e9

for i in range(1, M + 1):

    cases = list(itertools.combinations(chickens, i))

    for case in cases:
        chicken_street = [99 for _ in range(cnt)]

        for idx, home in enumerate(homes):
            for c in case:
                chicken_street[idx] = min(calc_street(home, c), chicken_street[idx])
                
        mins = min(mins, sum(chicken_street))

print(mins)