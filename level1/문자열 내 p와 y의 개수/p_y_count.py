def solution(s):
    answer = True
    p = 0
    y = 0
    
    for k in s:
        if k == 'p' or k == 'P':
            p = p + 1
        elif k == 'y' or k == 'Y':
            y = y + 1
    
    if p == y:
        answer = True
    else:
        answer = False

    return answer