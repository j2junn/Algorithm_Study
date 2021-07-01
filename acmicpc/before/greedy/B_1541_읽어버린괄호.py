import sys

formula = sys.stdin.readline().strip()

arr1 = formula.split('-')

num = []
for f in arr1:
    cnt = 0
    arr2 = f.split('+')

    for a in arr2:
        cnt += int(a)
    num.append(cnt)

n = num[0]

for i in range(1, len(num)):
    n -= num[i]

print(n)