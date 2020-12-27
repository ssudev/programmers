"""
    n : 학생수
    lost : 잃어버린 학생 번호(배열)
    reserve : 여벌의 체육복을 가지고 있는 학생 번호(배열)
"""
def solution(n, lost, reserve):
    answer = 0
    clothes = [1 for i in range(n+2)]

    for i in lost:
        clothes[i] = 0

    for i in reserve:
        clothes[i] += 1

    if n == 1:
        if clothes[1] > 0:
            return 1
        else:
            return 0
    
    for i in range(1,n+1):
        if clothes[i] > 1:
            
            if clothes[i-1] == 0 and i != 1:
                clothes[i-1] += 1
                clothes[i] -= 1
            elif clothes[i+1] == 0 and i != n:
                clothes[i+1] += 1
                clothes[i] -= 1

    for i in range(1,n+1):
        if clothes[i] > 0:
            answer += 1

    return answer