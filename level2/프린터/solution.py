def solution(priorities, location):
    answer = 0
    array = [False]*len(priorities)
    array[location] = True
    cnt = 0
    
    if len(priorities) == 1:
        answer = 1
        return answer
    
    while True:
        a = priorities[0]
        b = array[0]
        flag = True
        
        for i in range(1,len(priorities)):
            if a < priorities[i]:
                flag = False
                break
        
        if flag == False:
            priorities = priorities[1:]
            priorities.append(a)
            array = array[1:]
            array.append(b)
        else:
            cnt += 1
            if b:
                answer = cnt
                break

            priorities = priorities[1:]
            array = array[1:]

    return answer