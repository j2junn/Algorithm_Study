# 21-04-07

def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    # p2라는 str은 p1으로 시작하는지 검사
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1) == True:
            answer = False
    
    return answer