def solution(s, n):
    answer = ''
    
    for str in s:
        k = ord(str)

        if k >= 97 and k <= 122:
            if k + n > 122:
                k = k + n - 122 + 96
            else:
                k = k + n
            
            answer += chr(k)

        elif k >= 65 and k <= 90:
            if k + n > 90:
                k = k + n - 90 + 64
            else:
                k = k + n
            
            answer += chr(k)
        else:
            answer += str
        
    return answer