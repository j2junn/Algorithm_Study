N = int(input())
peoples = []
rank = []

for _ in range(N):
    peoples.append(list(map(int, input().split())))

for people in peoples:
    cnt = 0
    for p in peoples:
        if people == p:
            continue
        if people[0] < p[0] and people[1] < p[1]:
            cnt += 1
    
    rank.append(cnt + 1)

for r in rank:
    print(r, end=" ")