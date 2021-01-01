def solution(d, budget):
    answer = 0
    d.sort()
    num = 0
    
    for k in d:
        num += k
        answer += 1
        if num > budget:
            answer -= 1
            break
        elif num == budget:
            break
    
    return answer