tc = int(input())

for i in range(tc):
    N = float(input())
    
    j = -1
    n = ''
    while 1:
        if N >= 2**j:
            N -= 2**j
            n += str(1)
        else:
            n += str(0)
            
        j -= 1
        
        if N == 0.0:
            break
    
    if len(n) > 12:
        print("#{} overflow".format(i + 1))
    else:
        print("#{} {}".format(i + 1, n))
 