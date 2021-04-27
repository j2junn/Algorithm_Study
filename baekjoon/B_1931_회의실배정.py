import sys

answer = 0
N = int(sys.stdin.readline())
meeting = []

def greedy(meeting):
    cnt = 0
    start = 0
    
    for meet in meeting:
        if meet[0] >= start:
            start = meet[1]
            cnt += 1

    return cnt

for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    meeting.append([start, end])

meeting = sorted(meeting, key=lambda x: x[0])
meeting = sorted(meeting, key=lambda x: x[1])

print(greedy(meeting))

