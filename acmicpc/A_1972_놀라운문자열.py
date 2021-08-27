while True:
    flag = True
    answer = 'surprising.'
    
    words = input()
    if words == "*":
        break
    
    graphs = [[] for _ in range(len(words) + 1)]
    
    for i in range(len(words)):
        
        for j in range(0, len(words) - i - 1):
            if words[j+i+1] != None:
                graphs[i].extend(
                    [
                        words[j] + words[j + i + 1]
                     ]
                    )

    for graph in graphs:
        if len(graph) != len(set(graph)):
            flag = False     # 유일 x
            
    if flag == False:
        answer = "NOT surprising."
            
    print('{} is {}'.format(words, answer))