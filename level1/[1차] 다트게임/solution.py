def solution(dartResult):
    answer = 0
    point_array = [0,0,0,0]
    round = 0
    point = 0
    
    for i in range(len(dartResult)):
        s = dartResult[i]
        
        if s.isdigit():
            point = int(s)
            
            # 10 판단
            if s == '0' and i != 0 and '1' == dartResult[i-1]:
                point = 10
                
            # 10 판단
            if s == '1' and i != len(dartResult)-1 and '0' == dartResult[i+1]:
                continue
            
            round += 1
            
        if s == 'S' or s == 'D' or s == 'T':
            if s == 'S':
                point = point**1
            elif s == 'D':
                point = point**2
            elif s == 'T':
                point = point**3
            
            point_array[round] = point
        
        if s == '*' or s == '#':
            if s == '*':
                point_array[round] = point_array[round]*2
                point_array[round-1] = point_array[round-1]*2
            elif s == '#':
                point_array[round] = point_array[round]*(-1)
    
    answer = sum(point_array)
    
    return answer