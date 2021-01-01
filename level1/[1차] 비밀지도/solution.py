def binary(num,n):
    array = [0 for i in range(n)]
    
    if num == 0:
        array = array
    elif num == 1:
        array[n-1] = 1
    else:
        index = -1
        while True:
            k = num % 2
            num = int(num / 2)
            
            array[index] = k
            index = index -1
            if num < 2:
                array[index] = num
                break
    
    for i in range(len(array)):
        if array[i] == 0:
            array[i] = " "
        else:
            array[i] = "#"

    return array
    
    
def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        msg = ""
        k = binary(arr1[i],n)
        l = binary(arr2[i],n)
        
        for j in range(len(k)):
            if k[j] == "#" or l[j] == "#":
                msg += "#"
            else:
                msg += " "
        answer.append(msg)
        
    return answer