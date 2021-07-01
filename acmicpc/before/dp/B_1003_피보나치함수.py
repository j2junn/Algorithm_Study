import sys

fibo = [(1, 0), (0, 1), (1, 1), (1, 2)] + [(0, 0) for _ in range(37)]

for i in range(4, 41):
    fibo[i] = (fibo[i - 1][0] + fibo[i - 2][0], fibo[i - 1][1] + fibo[i - 2][1])

tc = int(sys.stdin.readline())

for _ in range(tc):
    n = int(sys.stdin.readline())
    
    print(fibo[n][0], fibo[n][1])