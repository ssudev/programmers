def solution(skill, skill_trees):
    answer = 0
    array_skill = [-1]*len(skill)

    for i in range(len(skill_trees)):
        word = skill_trees[i]
        
        for j in range(len(skill)):
            skill_s = skill[j]
            
            if skill_s in word:
                array_skill[j] = word.find(skill_s)

        # skill이 다 없는경우
        if sum(array_skill) == len(array_skill)*(-1):
            print("answer ",end=" ")
            answer += 1
        elif len(array_skill) == 1:
            print("answer ",end=" ")
            answer += 1
        elif array_skill[0] != -1:
            f_num = array_skill[0]
            flag = True

            for j in range(1,len(array_skill)):
                t_num = array_skill[j]

                if f_num == -1 and t_num != -1:
                    flag = False
                    break

                if f_num != -1 and t_num != -1 and f_num > t_num:
                    flag = False
                    break
                
                f_num = t_num
            
            if flag:
                print("answer ",end=" ")
                answer += 1
        
        print(array_skill)
        array_skill = [-1]*len(skill)

    return answer

def solution2(skill, skill_trees):
    arr = []
    nums = 0

    for i in range(len(skill)):
        arr.append(skill[0:i+1])
    
    print(arr)

    for i in skill_trees:
        brr =""
        for j in i:
            if j in skill:
                brr += j
        if brr in arr:
            nums += 1
    return nums