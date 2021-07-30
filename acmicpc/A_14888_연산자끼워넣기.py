import itertools

N = int(input())
A = list(map(int, input().split()))
operators = list(map(int, input().split()))
opList = ['+', '-', '*', '/']
op = []

for i in range(4):
    for _ in range(operators[i]):
        op.append(opList[i])
        
maximum = float('-inf')
minimum = float('inf')

for case in itertools.permutations(op, N - 1):
    total = A[0]
    
    for i in range(1, N):
        if case[i - 1] == '+':
            total += A[i]
        elif case[i - 1] == '-':
            total -= A[i]
        elif case[i - 1] == '*':
            total *= A[i]
        elif case[i - 1] == '/':
            total = int(total / A[i])
            
    if total > maximum:
        maximum = total
    if total < minimum:
        minimum = total
            
print(maximum)
print(minimum)