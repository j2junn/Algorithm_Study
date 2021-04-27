import sys

answer = 0

N = int(sys.stdin.readline())

people = list(map(int, sys.stdin.readline().split()))

people = sorted(people)

for i in range(N):
    answer += sum(people[0:i + 1])

print(answer)