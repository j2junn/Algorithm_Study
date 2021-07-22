tc = int(input())

for i in range(tc):
    c = int(input())
    scores = list(map(int, input().split()))
    
    sets = {}
    
    for score in scores:
        sets[score] = sets.get(score, 0) + 1
    
    print("#{} {}".format(i+1, sorted(sets.items(), key=lambda x: x[1], reverse=True)[0][0]))
