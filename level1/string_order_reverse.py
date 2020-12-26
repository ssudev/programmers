"""
    https://programmers.co.kr/learn/courses/30/lessons/12917

    예시
    s	        return
    Zbcdefg	    gfedcbZ
"""

def solution(s):
    answer = sorted(s, reverse = True)
    
    return ''.join(answer)