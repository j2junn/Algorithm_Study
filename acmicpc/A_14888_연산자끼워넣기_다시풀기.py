N = int(input())
arr = list(map(int, input().split()))
operators = list(map(int, input().split()))

mx, mn = -1e9, 1e9

def DFS(idx, result, plus, minus, multiple, divide):
    global mx, mn
    
    if idx == N:
        mx = max(mx, result)
        mn = min(mn, result)
    
    if plus > 0:
        DFS(idx + 1, result + arr[idx], plus - 1, minus, multiple, divide)
    if minus > 0:
        DFS(idx + 1, result - arr[idx], plus, minus - 1, multiple, divide)
    if multiple > 0:
        DFS(idx + 1, result * arr[idx], plus, minus, multiple - 1, divide)
    if divide > 0:
        DFS(idx + 1, int(result / arr[idx]), plus, minus, multiple, divide - 1)
      
    
DFS(1, arr[0], operators[0], operators[1], operators[2], operators[3])

print("{}\n{}".format(mx, mn))