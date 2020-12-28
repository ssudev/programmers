def solution(n):
    answer = 0
    
    l = str(n)
    
    for i in l:
        answer += int(i)
    
    return answer