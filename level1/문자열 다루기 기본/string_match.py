def solution(s):
    answer = True
    
    if s.isdigit():
        answer = True
    else:
        answer = False
    
    if len(s) < 4 or len(s) > 6 or len(s) == 5:
        answer = False
    
    return answer