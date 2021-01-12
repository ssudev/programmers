def gcd(w,h):
    if w < h:
        t = w
        w = h
        h = t
    while h:
        w,h = h,w%h
    return w

def solution(w,h):
    k = gcd(w,h)
    answer = w*h-(int(w/k)+int(h/k)-1)*k
    
    return answer