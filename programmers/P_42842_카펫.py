def solution(brown, yellow):
    answer = []
    
    t = brown + yellow
    
    for i in range(t, 0, -1):
        if t % i == 0:
            w, h = i, t // i
            if w >= h and (w - 2) * (h - 2) == yellow:
                return [w, h]