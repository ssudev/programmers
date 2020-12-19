"""
https://programmers.co.kr/learn/courses/30/lessons/68935

예시 :
    45 / 3 = 15 ... 0
    15 / 3 = 5 ... 0
    5 / 3 = 1 ... 2

    125 / 3 = 41 ... 2
    41 / 3 = 13 ... 2
    13 / 3 = 4 ... 1
    4 / 3 = 1 ... 1

    3 / 3 = 1 ... 0
"""

def solution(n):
    answer = 0
    array = []

    if n == 1:
        array.append(1)
    elif n == 2:
        array.append(2)
    else:
        while True:
            k = int(n % 3)
            n = int(n / 3)

            array.append(k)

            if n < 3:
                array.append(n)
                break

    array.reverse()

    j = 1
    for i in array:
        answer = answer + i * j
        j = j * 3

    return answer