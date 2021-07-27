T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    n = list(map(int, input().split()))
    m = list(map(int, input().split()))
    
    n.sort(reverse=True)
    m.sort(reverse=True)
    
    answer = 0
    
    i = j = 0
    
    while 1:
        if i == N or j == M:
            break

        if n[i] <= m[j]:
            answer += n[i]
            i += 1
            j += 1
        else:
            i += 1
    
    print("#{} {}".format(t + 1, answer))
    