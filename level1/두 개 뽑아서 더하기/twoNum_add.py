"""
    https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3

    예시
    numbers	    result
    [2,1,3,4,1]	[2,3,4,5,6,7]
    [5,0,2,7]	[2,5,7,9,12]

"""
def solution(numbers):
    answer = []
    answer2 = []

    for idx, num in enumerate(numbers):
        for j in range(idx+1, len(numbers)):
            result = num + numbers[j]
            answer.append(result)

    for v in answer:
        if v not in answer2:
            answer2.append(v)
    answer2.sort()
    return answer2