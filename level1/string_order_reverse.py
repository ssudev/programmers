"""
    https://programmers.co.kr/learn/courses/30/lessons/12917

    예시
    s	        return
    Zbcdefg	    gfedcbZ

    파이썬의 정렬은 2가지
    sorted()
    .sort()
"""

def solution(s):
    answer = sorted(s, reverse = True)
    
    return ''.join(answer)