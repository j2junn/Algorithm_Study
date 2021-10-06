import heapq

N = int(input())
h = []

# N개 먼저 push
for n in map(int, input().split()):
    heapq.heappush(h, n)

# N-1 번 반복하면서 입력과 동시에 받아서 heapq에 push하고 pop 반복(N개 유지하도록)
for _ in range(N - 1):
    for n in map(int, input().split()):
        heapq.heappush(h, n)
        heapq.heappop(h)

# heapq 중에서 가장 작은 숫자 = N번째로 큰 숫자 출력
print(heapq.heappop(h))