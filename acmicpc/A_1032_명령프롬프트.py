N = int(input())
patterns = [input() for _ in range(N)]
patterns = sorted(patterns)

if N == 1:
    print(patterns[0])
    exit
else:
    answer = ''

    start = patterns[0]
    length = len(start)

    answer = list(start)

    for i in range(1, N):
        for j in range(length):
            if start[j] != patterns[i][j]:
                answer[j] = '?'            

    print(''.join(answer))