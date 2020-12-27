"""
    https://programmers.co.kr/learn/courses/30/lessons/12919

    예시
    seoul	    return
    [Jane, Kim]	김서방은 1에 있다
"""

def solution(seoul):
    answer = ''
    
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            answer = '김서방은 ' + str(i) + '에 있다'
    
    return answer