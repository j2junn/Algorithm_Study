import itertools

answer = []

# L: 암호의 자리수
# C: 알파벳 개수
L, C = map(int, input().split())

alphbets = list(input().split())

# 전체에서 L개 만큼 뽑는 경우의 수(문자는 같은데 순서만 다르다면, 같은 경우로(Combi))
cases = list(itertools.combinations(alphbets, L))

for case in cases:
    # case = list(case)
    cnt = 0
    # 모음 검사
    for c in case:
        if c in ['a', 'e', 'i', 'o', 'u']:
            cnt += 1

    if 0 < cnt < L - 1:
        answer.append(''.join(sorted(case)))
        
for a in sorted(answer):
    print(a)