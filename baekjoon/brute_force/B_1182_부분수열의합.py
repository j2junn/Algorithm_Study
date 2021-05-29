import sys
from itertools import combinations

answer = 0

N, S = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

for i in range(N, 0, -1):
    cb = list(combinations(nums, i))
    
    for j in cb:
        if sum(j) == S:
            answer += 1
   
print(answer)