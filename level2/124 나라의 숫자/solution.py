def solution(n):
    answer = ''
    
    while True:
        a = int(n/3)
        b = int(n%3)
        c = 0
        if b == 0:
            c = 1
            answer = '4' + answer
        else:
            answer = str(b) + answer
        
        n = a - c
        
        if n < 1:
            break
        
    return answer