import sys

# 필요한 감독관의 최소 수
answer = 0

N = int(sys.stdin.readline())
rooms = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

# 문제에서는 총감독관이 반드시 필요하다는 말이 안적혀있어서 몰랐지만
# 예제4번을 보고 깨달았고 모든 시험장 N개에는 총감독관 1명씩 전부다 들어가므로 

# rooms라는 전체 리스트에서 각각에 B를 뺀 나머지로 다시 저장
rooms = list(map(lambda r: r - B, rooms))

# 그 후, answer에 N을 더해줌
answer += N

for room in rooms:
    if room > 0:
        if room % C == 0:
            answer += room // C
        else:
            answer += room // C + 1

print(answer)