def print_matrix(mat):
    m = len(mat)
    n = len(mat[0])
    for i in range(m-1,-1,-1):
        for j in range(n-1,0,-1):
            mat[i][j] -=mat[i][j-1]
    
    for i in range(m-1,0,-1):
        for j in range(n-1,-1,-1):
            mat[i][j] -=mat[i-1][j] 
    
    return mat


after = [[2, 5], [7, 17]]
print(print_matrix(after))