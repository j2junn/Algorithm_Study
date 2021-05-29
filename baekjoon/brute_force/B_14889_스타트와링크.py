import sys
import itertools

N = int(sys.stdin.readline())
arr = []
sum = []

for _ in range(N):
    n = list(map(int, sys.stdin.readline().split()))
    arr.append(n)
    
cbs = itertools.combinations(range(N), N//2)

diff = float('inf')

for cb in cbs:
    teamA = set(cb)
    teamB = set(range(N)) - set(cb)
  
    teamA_sub = itertools.combinations(teamA, 2)
    teamB_sub = itertools.combinations(teamB, 2)
  
    sumA = 0
    sumB = 0
    
    for a in teamA_sub:
        sumA += (arr[a[0]][a[1]] + arr[a[1]][a[0]])
    
    for b in teamB_sub:
        sumB += (arr[b[0]][b[1]] + arr[b[1]][b[0]])
    
    if abs(sumA - sumB) < diff:
        diff = abs(sumA - sumB)
    
print(diff)