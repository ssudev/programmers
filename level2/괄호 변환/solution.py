def isPerfect(p):
    a = []
    for s in p:
        a.append(s)

        if len(a) >= 2:
            if a[-1] == ')' and a[-2] == '(':
                a.pop(); a.pop()

    if len(a) == 0:
        return True
    else:
        return False

def solution(p):
    answer = ''
    u = ""
    v = ""
    left = 0
    right = 0

    if len(p) == 0 or isPerfect(p):
        return p

    for i in range(len(p)):
        s = p[i]
        if s == "(":
            left += 1
        else:
            right += 1

        if left == right:
            u = p[:i+1]
            v = p[i+1:len(p)]
            break
    
    if isPerfect(u):
        answer += u + solution(v)
    else:
        answer += "(" + solution(v) + ")"
        for s in u[1:-1]:
            if s == "(":
                answer += ")"
            else:
                answer += "("

    return answer