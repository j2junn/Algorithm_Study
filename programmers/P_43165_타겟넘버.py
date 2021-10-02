# Solution 1 - Product 이용
from itertools import product
def solution(numbers, target):
    answer = 0
    
    # numbers의 len이 5라면
    # [(1, -1), (1, -1), (1, -1), (1, -1), (1, -1)]
    l = [(x, -x) for x in numbers]
    
    # *l : unpacking의 의미이다.
    # 즉, *l = (1, -1), (1, -1), (1, -1), (1, -1), (1, -1)
    # product: 데카르트 곱(cartesian product)
    # ex) list = ['ab','cd']
    # -> product(*list) = [('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd')]
    s = list(map(sum, product(*l)))
    
    return s.count(target)

# Solution 2 - DFS 이용
answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    
    if idx == N and target == value:
        answer += 1
        return
    elif idx == N:
        return
    
    DFS(idx + 1, numbers, target, value + numbers[idx])
    DFS(idx + 1, numbers, target, value - numbers[idx])
        
def solution(numbers, target):
    global answer
    
    DFS(0, numbers, target, 0)
    
    return answer