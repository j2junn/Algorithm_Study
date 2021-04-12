# 21-04-08

def solution(n, lost, reserve):
    answer = 0
    nn = [i for i in range(1, n + 1)]
    # 완벽하게 수업을 들을 수 있는 학생들 list
    nn = set(nn).difference(set(lost))
    nn = list(nn.union(set(reserve)))
    
    # 여별옷이 있는데 도난당해서 못빌려주는 진짜 학생들 : real_reserve
    # 도난당했는데 여벌옷이 있는 애들을 제외한 진짜 도난당한 학생들 : real_lost
    intersection = list(set(reserve).intersection(set(lost)))
    real_reserve = list(set(reserve) - set(intersection))
    real_lost = list(set(lost) - set(intersection))

    # 도난당한 학생이 여별옷을 빌릴 수 있을 경우
    # 그 학생은 수업을 들을 수 있으니까 nn에 append
    # 그리고 빌려준 학생은 이제 다른 학생을 못빌려주니까 reserve에서 remove
    for l in real_lost:
        if l - 1 in real_reserve:
            nn.append(l)
            real_reserve.remove(l - 1)           
        elif l + 1 in real_reserve:
            nn.append(l)
            real_reserve.remove(l + 1)
            
    return len(nn)