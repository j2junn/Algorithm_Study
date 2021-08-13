import itertools

pattern1 = [1, 2, 3, 4, 5]
pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

def solution(answers):
    answer = []
    cnt = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == pattern1[i % 5]:
            cnt[0] += 1
        if answers[i] == pattern2[i % 8]:
            cnt[1] += 1
        if answers[i] == pattern3[i % 10]:
            cnt[2] += 1
    
    mx = max(cnt)
    
    for idx, c in enumerate(cnt):
        if mx == c:
            answer.append(idx + 1)

    return answer