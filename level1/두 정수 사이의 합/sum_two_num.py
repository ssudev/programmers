"""

    https://programmers.co.kr/learn/courses/30/lessons/12912
    
    - 예시
    a : 3
    b : 5
    return : 12
"""

def solution(a, b):
    answer = 0
    
    if a == b:
        answer = a
    else:
        if a > b:
            for i in range(b,a+1):
                answer += i
        else:
            for i in range(a,b+1):
                answer += i
            
    return answer