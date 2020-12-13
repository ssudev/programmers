# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    
    for temp_commands in commands:
        temp_array = array[temp_commands[0]-1:temp_commands[1]]
        temp_array.sort()
        answer.append(temp_array[temp_commands[2]-1])

    return answer