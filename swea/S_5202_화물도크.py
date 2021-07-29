T = int(input())
for t in range(T):
    N = int(input())
    data = []
    
    for _ in range(N):
        data.append(list(map(int, input().split())))
        
    data.sort(key=lambda x: x[1])
    cnt = 0
    end = data.pop(0)[1]
        
    while data:
        now = data.pop(0)
        if end <= now[0]:
            end = now[1]
            cnt += 1
    
    print("#{} {}".format(t + 1, cnt + 1))