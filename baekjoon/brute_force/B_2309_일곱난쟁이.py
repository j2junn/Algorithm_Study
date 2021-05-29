import sys
import itertools

arr = []
arr_idx = [i for i in range(9)]

for i in range(9):
    arr.append(int(sys.stdin.readline()))

arr_sum = sum(arr)

# nPr = itertools.permutations(arr_idx, 2)
nCr = itertools.combinations(arr_idx, 2)

for a in list(nCr):
    if arr_sum - arr[a[0]] - arr[a[1]] == 100:

        flag1 = arr[a[0]]
        flag2 = arr[a[1]]

        break

for a in sorted(arr):
    if a != flag1 and a != flag2:
        print(a)