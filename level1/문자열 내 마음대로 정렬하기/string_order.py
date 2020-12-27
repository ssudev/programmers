def solution(strings, n):
    answer = []
    strings.sort()
    answer.append(strings[0])

    if len(strings) == 1:
        return answer

    for i in range(1,len(strings)):
        temp = strings[i][n:n+1]

        j = 0
        while True:
            temp2 = answer[j][n:n+1]

            if temp < temp2:
                answer.insert(j,strings[i])
                break

            j = j + 1
            if j >= len(answer):
                answer.append(strings[j])
                break


    return answer

def solution2(strings, n):
    strings.sort()
    return sorted(strings, key=lambda string: string[n:n+1])