"""
    https://programmers.co.kr/learn/courses/30/lessons/12901
    datetime 모듈을 활용하여 요일 구하기
"""
import datetime

def solution(a, b):
    week = ['MON','TUE','WED','THU','FRI','SAT','SUN']

    a = datetime.date(2016,a,b).weekday()
    return week[a]


