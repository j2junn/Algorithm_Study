def solution(triangle):
    
    # triangle 아래부터 위로
    for i in range(len(triangle) - 1, 0, -1):
        
        for j in range(len(triangle[i]) - 1):
            
            triangle[i - 1][j] += max(triangle[i][j], triangle[i][j + 1])
    
    
    return triangle[0][0]