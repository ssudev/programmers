def solution(s):
    answer = s
    tempAnswer = s

    nowAindex = 1
    nowBindex = 1
    for i in range(1,int(len(s)/2) + 1):
        # 초기화
        if(len(answer) >= len(tempAnswer)):
            answer = tempAnswer

        tempAnswer = ""
        preCnt = 1
        nowAindex = i
        nowBindex = i * 2 
        now = s[nowAindex:nowBindex]
        pre = s[0:nowAindex]

        while nowBindex <= len(s):

            if now == pre:
                preCnt += 1 
            else:
                if preCnt == 1:
                    tempAnswer += pre
                else:
                    tempAnswer += str(preCnt) + pre
                preCnt = 1

            pre = now
            nowAindex += i
            nowBindex += i
            if nowBindex > len(s):
                if preCnt == 1:
                    tempAnswer += s[nowAindex-i:]
                else:
                    tempAnswer += str(preCnt) + s[nowAindex-i:]
                break

            now = s[nowAindex:nowBindex]

    if(len(answer) >= len(tempAnswer)):
        answer = tempAnswer

    return len(answer)