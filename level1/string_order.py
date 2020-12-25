"""
    https://programmers.co.kr/learn/courses/30/lessons/12915

    문자열 내 마음대로 정렬하기
    예시
    strings	            n	return
    [sun, bed, car]	    1	[car, bed, sun]
    [abce, abcd, cdx]	2	[abcd, abce, cdx]

    쉽게 정렬하는 법
    sorted(strings, key=lambda string: string[n:n+1])
"""

def solution(strings, n):
    answer = []
    strings.sort()
    answer.append(strings[0])

    if len(strings) == 1:
        return answer

    for i in range(1,len(strings)):
        temp = strings[i][n:n+1]

        j = 0
        while True:
            temp2 = answer[j][n:n+1]

            if temp < temp2:
                answer.insert(j,strings[i])
                break

            j = j + 1
            if j >= len(answer):
                answer.append(strings[j])
                break


    return answer

def solution2(strings, n):
    strings.sort()
    return sorted(strings, key=lambda string: string[n:n+1])