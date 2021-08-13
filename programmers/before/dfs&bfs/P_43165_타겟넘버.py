def DFS(idx, numbers, target, num):
    global answer
    
    if idx == len(numbers) and num == target:
        answer += 1
        return
    
    if idx == len(numbers):
        return
    
    DFS(idx + 1, numbers, target, num + numbers[idx])
    DFS(idx + 1, numbers, target, num - numbers[idx])


answer = 0

def solution(numbers, target):
    
    DFS(0, numbers, target, 0)
    
    return answer
