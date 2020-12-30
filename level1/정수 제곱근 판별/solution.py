def solution(n):
    answer = 0
    
    k = int(n**0.5)
    k2 = int(k**2)
    
    if n == k2:
        answer = (k + 1)**2
    else:
        answer = -1
    
    return answer