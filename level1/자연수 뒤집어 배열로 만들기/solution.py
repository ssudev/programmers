def solution(n):
    answer = []
    
    s = str(n)
    
    for k in range(len(s)-1,-1,-1):
        answer.append(int(s[k]))
    
    return answer