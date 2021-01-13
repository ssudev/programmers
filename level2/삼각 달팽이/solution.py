def solution(n):
    array = [[0 for i in range(n)] for j in range(n)]
    
    cnt = 1
    x = 0; y = 0
    x1 = 1; y1 = 0
    x2 = 0; y2 = 1
    x3 = -1; y3 = -1
    array[x][y] = cnt
    endCnt = 0
    
    for i in range(1,n):
        endCnt += i
    endCnt = n*n - endCnt
    answer = [0 for i in range(endCnt)]
    
    if n == 1:
        return [1]
    
    while True:
        
        # 아래로만 가는경우
        while True:
            
            if x + x1 < n and y + y1 < n and array[x+x1][y+y1] == 0:
                x += x1 ; y += y1
                cnt += 1
                array[x][y] = cnt
            else:
                break
        
        
        # 오른쪽으로만 가는 경우
        while True:
            
            if x + x2 < n and y + y2 < n and array[x+x2][y+y2] == 0:
                x += x2 ; y += y2
                cnt += 1
                array[x][y] = cnt
            else:
                break
        
        # 왼쪽 대각선으로만 가는 경우
        while True:
            
            if x + x3 < n and y + y3 < n and array[x+x3][y+y3] == 0:
                x += x3 ; y += y3
                cnt += 1
                array[x][y] = cnt
            else:
                break
        
        if cnt == endCnt:
            break
   
    cnt = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] != 0:
                answer[cnt] = array[i][j]
                cnt += 1
    
    return answer