tc = int(input())

for i in range(tc):
    N = int(input())
    prices = list(map(int, input().split()))
    prices = prices[::-1]
    answer = 0
    
    max_value = prices[0]
    
    for j in range(1, N):
        if prices[j] < max_value:
            answer += max_value - prices[j]
        else:
            max_value = prices[j]
    
    print("#{} {}".format(i + 1, answer))