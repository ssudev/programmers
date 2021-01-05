def solution(progresses, speeds):
    answer = []
    array = [0]*len(progresses)

    for i in range(len(progresses)):
        a = progresses[i]
        b = speeds[i]
        cnt = 0
        while True:
            a = a + b
            cnt += 1
            if a >= 100:
                array[i] = cnt
                break

    if len(array) == 1:
        answer.append(1)
        return answer

    a = array[0]
    cnt = 1
    for i in range(1,len(array)):
        k = array[i]

        if a >= k:
            cnt += 1
        else:
            a = k
            answer.append(cnt)
            cnt = 1

        if i == len(array)-1:
            answer.append(cnt)

    return answer