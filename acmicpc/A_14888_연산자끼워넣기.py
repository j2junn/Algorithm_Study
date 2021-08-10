import itertools

N = int(input())
operands = list(map(int, input().split()))
operators = list(map(int, input().split()))

mx, mn = -1e9, 1e9

def solve(idx, ans, add, sub, mul, div):
    global mx, mn
    
    if idx == N:
        mx = max(mx, ans)
        mn = min(mn, ans)
    
    if add:
        solve(idx + 1, ans + operands[idx], add - 1, sub, mul, div)
    if sub:
        solve(idx + 1, ans - operands[idx], add, sub - 1, mul, div)
    if mul:
        solve(idx + 1, ans * operands[idx], add, sub, mul - 1, div)
    if div:
        solve(idx + 1, int(ans / operands[idx]), add, sub, mul, div - 1)
        
        
solve(1, operands[0], operators[0], operators[1], operators[2], operators[3])
print("{}\n{}".format(mx, mn))