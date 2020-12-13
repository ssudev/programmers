# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    dic = [0,0,0]
    answer_1 = [1,2,3,4,5]
    answer_2 = [2,1,2,3,2,4,2,5]
    answer_3 = [3,3,1,1,2,2,4,4,5,5]
    
    1,2,3,4,5,6,7,8,9,10
    
    for i in range(len(answers)):
        
        index = i%5
        if answers[i] == answer_1[index]:
            dic[0] += 1
        
        index = i%8
        if answers[i] == answer_2[index]:
            dic[1] += 1
            
        index = i%10
        if answers[i] == answer_3[index]:
            dic[2] += 1
    
    for i in range(len(dic)):
        if max(dic) == dic[i]:
            answer.append(i+1)
    
    
    return answer