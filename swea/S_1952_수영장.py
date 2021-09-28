def solve(month, sum):
    global answer
    if month > 11:
        if answer > sum:
            answer = sum
            return
        return

    if plans[month] == 0:
        solve(month + 1, sum)
    else:
        solve(month + 1, plans[month] * prices[0] + sum)
        
        solve(month + 1, prices[1] + sum)
        
        solve(month + 3, prices[2] + sum)
    

T = int(input())
for i in range(T):
    prices = list(map(int, input().split()))
    plans = list(map(int, input().split())) 
   
    answer = prices[3]
    solve(0, 0)
    print("#{} {}".format(i+1, answer))
