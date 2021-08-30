T = int(input())

for _ in range(T):
    answer = ''
    R, S = input().split()
    R = int(R)
    
    for s in S:
        words = [s for _ in range(R)]
        answer += ''.join(words)

    print(answer)