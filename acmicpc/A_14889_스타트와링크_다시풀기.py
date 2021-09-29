import itertools

def calc_power(team):
    power = 0
    
    for i in range(N//2 - 1):
        for j in range(i + 1, N//2):
            power += ability[team[i]][team[j]] + ability[team[j]][team[i]]
    
    return power

N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]
humans = [i for i in range(N)]

minm = float('inf')

cases = list(itertools.combinations(humans, N//2))
for case in cases:
    team1 = list(case)
    team2 = list(set(humans) - set(team1))
    
    minm = min(abs(calc_power(team1) - calc_power(team2)), minm)

print(minm)