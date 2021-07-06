import sys
from itertools import permutations, combinations

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
    
    
def calc2(i, j):
    return graph[i][j] + graph[j][i]

# 전달받은 각 팀의 원소 중에 2개씩을 다시 C(조합)을 구함
# why? N이 4라면 2개씩 바로 구할 수 있지만 6부터는 (1, 2, 3), (1, 2, 4), ... 이렇게 나오므로
# 다시 (1, 2), (1, 3), (2, 3) ... 두개를 뽑아서 능력치 구하는 식(calc2 함수)에 넣어서 진짜 두 팀의 능력치(score1, score2)를 구함
# 두 팀의 능력치의 절대값을 반환
def calc1(team1, team2):
    team1 = list(combinations(team1, 2))
    team2 = list(combinations(team2, 2))
    score1 = 0
    score2 = 0
    
    for t1 in team1:
        score1 += calc2(t1[0], t1[1])
        
    for t2 in team2:
        score2 += calc2(t2[0], t2[1])
    
    return abs(score1 - score2)

# N의 max가 20이므로 C(조합)의 최대 개수는 184,756일 것이므로
# 먼저 전체 중에 두 팀으로 나누는 경우를 모두 구함
num = [i for i in range(N)]
combi = list(combinations(num, N//2))
combi_len = len(combi)

# C(조합)을 구한 것 중 첫번째와 마지막, 두번째와 마지막 - 1 ... 이렇게 두 팀으로 묶을 수 있음
# ex) N이 4일때 [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)] 이렇게 C(조합)을 구함
# (1, 2)랑 (3, 4)를, (1, 3)과 (2, 4)를, (1, 4)와 (2, 3)으로 calc1함수로 전달해줌
answer = []
for i in range(combi_len // 2):
    answer.append(calc1(combi[i], combi[combi_len - 1 - i]))

# 반환된 절대값들을 한 리스트에 넣고 min값을 출력
print(min(answer))
