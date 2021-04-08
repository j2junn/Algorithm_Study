# 21-04-07

def solution(participant, completion):
    answer = ''
    
    d = {}
    
    # get: key로 value를 얻어내는 함수
    # d.get(p): p라는 key의 value 출력
    # d.get(p, 0): p라는 key의 value가 없으면 0으로 출력
    for p in participant:
        d[p] = d.get(p, 0) + 1
    
    for c in completion:
        d[c] -= 1
            
    for k, v in d.items():
        if v == 1:
            return k
        