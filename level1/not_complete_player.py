# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    dic = {}
    
    for completionName in completion:
        if completionName in dic:
            dic[completionName] += 1
        else:
            dic[completionName] = 1
    
    for participantName in participant:
        if participantName in dic:
            dic[participantName] -= 1
            
            if dic[participantName] < 0:
                return participantName
        else:
            return participantName