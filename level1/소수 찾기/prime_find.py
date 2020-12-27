"""
    https://programmers.co.kr/learn/courses/30/lessons/12921

    에라토스테네스의 체
    - https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
    - 2부터 시작하여 배수가 되는 부분을 전부다 뺀다
    - 시작 범위는 m^2 > n 만큼 즉, m = int(n ** 0.5)

    예시
    n	result
    10	4
    5	3
"""

def solution(n):
    answer = 0
    array = [True] * (n+1)
    
    m = int(n ** 0.5)
    
    for i in range(2,m+1):
        if array[i] == True:
            for j in range(i+i,n+1,i):
                array[j] = False
    
    for i in range(2,n+1):
        if array[i] == True:
            answer += 1
    
    return answer