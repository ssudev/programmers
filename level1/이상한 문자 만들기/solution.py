def solution(s):
    answer = ''
    
    array = s.split(' ')
    
    for str in array:
        for i in range(len(str)):
            if i % 2 == 0:
                answer += str[i].upper()
            else:
                answer += str[i].lower()
        answer += ' '
    
    answer = answer[:len(answer)-1]
    
    return answer