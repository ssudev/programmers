def solution(x):
    answer = True
    
    int_x = 0
    str_x = str(x)
    
    for k in str_x:
        int_x += int(k)
    
    if x % int_x == 0:
        answer = True
    else:
        answer = False
    
    return answer