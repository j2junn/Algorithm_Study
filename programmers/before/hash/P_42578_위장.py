# 21-04-07

def solution(clothes):
    answer = 1
    
    dic = {}
    
    # k라는 key의 value가 없으면 0, 있으면 불러와서 1씩 더해줌
    for v, k in clothes:
        dic[k] = dic.get(k, 0) + 1
    
    # 종류의 개수 + 1 중에 1개를 뽑을 수 있도록 함(안뽑는경우도 고려)
    for v in dic.values():
        answer *= v + 1
    
    # 의상이 최소 한 개 이상 있어야 하므로 해당 경우 1을 빼줌
    return answer - 1