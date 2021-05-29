import sys

answer = 0

# 시험장의 개수
N = int(sys.stdin.readline())

rooms = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())


rooms = list(map(lambda r: r - B, rooms))

for room in rooms:
    if room > 0:
        if room % C == 0:
            answer += room // C
        else:
            answer += room // C + 1

print(len(rooms) + answer)

