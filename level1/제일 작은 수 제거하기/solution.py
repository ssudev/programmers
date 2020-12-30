def solution(arr):
    answer = []
    
    if len(arr) == 1:
        answer.append(-1)
        return answer
    
    min = arr[0]
    index = 0
    
    for i in range(1,len(arr)):
        if min > arr[i]:
            min = arr[i]
            index = i
    
    arr.pop(index)
    answer = arr
    
    return answer