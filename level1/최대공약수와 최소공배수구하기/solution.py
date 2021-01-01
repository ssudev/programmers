# gcd 
def gcd(n, m):
    if n > m:
        n,m = m,n
    if m % n == 0:
        return n
    
    return gcd(n, m%n)

def solution(n, m):
    k = gcd(n,m)
    l = n * m /gcd(n,m)
    
    answer = []
    answer.append(k)
    answer.append(l)
    return answer