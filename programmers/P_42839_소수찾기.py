import itertools, math

def is_prime_number(x):
    if x < 2:
        return False
    
    for i in range(2, x):
        if x % i == 0:
            return False
        
    return True


def solution(numbers):
    answer = []
    cases = []
    
    for i in range(1, len(numbers) + 1):
        cases.append(list(itertools.permutations(list(numbers), i)))
    
    for case in cases:
        for c in set(case):
            if is_prime_number(int(''.join(c))):
                answer.append(int(''.join(c)))
        
    return len(set(answer))