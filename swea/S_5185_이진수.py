def bin(n):
    t = ''
    for i in range(4):
        t = str(n % 2) + t
        n = n // 2
    
    return t

temp = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

tc = int(input())
for i in range(tc):
    n, nums = input().split()
    answer = ''

    for num in nums:
        if num in temp:
            now = temp[num]
        else:
            now = int(num)
        
        answer += bin(now)
    
    print("#{} {}".format(i + 1, answer))