"""
    https://programmers.co.kr/learn/courses/30/lessons/12906

    예시
    arr	            answer
    [1,1,3,3,0,1,1]	[1,3,0,1]
    [4,4,4,3,3]	    [4,3]
"""

def solution(arr):
    answer = []
    temp = -1
    for i in arr:
        if i != temp:
            answer.append(i)
            temp = i
    
    return answer