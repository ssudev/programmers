def solution(N, stages):
    answer = []
    fail_array = [0 for i in range(N+1)]
    fail_dic = {}
    cnt = 0
    
    for i in stages:
        if i > N:
            continue
        fail_array[i] += 1
    
    for i in range(1,len(fail_array)):
        if cnt == len(stages):
            fail_dic[i] = 0
            continue
            
        fail_dic[i] = fail_array[i] / (len(stages) - cnt) 
        cnt += fail_array[i]
    
    answer = sorted(fail_dic.keys(), key = lambda x:fail_dic[x], reverse=True)
    
    return answer