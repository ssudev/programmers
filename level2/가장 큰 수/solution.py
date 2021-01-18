def solution(numbers):
    answer = ''
    dic = {}
    
    if sum(numbers) == 0:
        return '0'
    
    for i in range(len(numbers)):
        num = numbers[i]
        l = str(num)
        if num == 0:
            dic[i] = num
        elif num == 1000:
            dic[i] = num
        else:
            k = num
            while True:
                k = str(k) + str(k)
                
                if len(k) > 4:
                    k = k[0:4]
                    break
            dic[i] = int(k)
    
    array = sorted(dic.items(), key = lambda x:x[1],reverse = True)
    for k in array:
        answer += str(numbers[k[0]])
    
    return answer