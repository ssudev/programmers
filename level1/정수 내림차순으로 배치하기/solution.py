def solution(n):
    answer = 0
    array = []
    s = str(n)
    
    for k in s:
        array.append(k)
    
    array.sort(reverse = True)
    answer = int("".join(array))
    
    return answer