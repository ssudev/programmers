def solution(n):
    answer = 0
    
    if n == 1:
        return 1
    
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            if n / i == i:
                answer += i
            else:
                answer += i + int(n/i)
    
    return answer