def solution(num):
    answer = 0
    cnt = 0
    
    if num == 1:
        return 0

    while True:
        if num % 2 == 0:
            num = num / 2    
        else:
            num = num * 3 + 1
        cnt += 1
        
        if num == 1:
            break
        
        if cnt == 500:
            break
    
    if cnt == 500:
        answer = -1
    else:
        answer = cnt
    
    return answer