import sys

answer = 0

# 시험장의 개수
N = int(sys.stdin.readline())

rooms = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())


rooms = list(map(lambda r: r - B, rooms))

for room in rooms:
    if room % C != 0:
        answer += int(room / C) + 1
    else:
        answer += int(room / C)

print(len(rooms) + answer)

