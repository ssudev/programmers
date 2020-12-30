def solution(numbers, hand):
    answer = ''
    left_point = {"x" : 4, "y" : 1}
    right_point = {"x" : 4, "y" : 3}
    keypad = [[-1,-1,-1,-1],[-1,1,2,3],[-1,4,5,6],[-1,7,8,9],[-1,-1,0,-1]]
    
    for num in numbers:
        for k in range(1,len(keypad)):
            for j in range(1,len(keypad[k])):
                
                if keypad[k][j] == num:
                    
                    if num in (2,5,8,0):
                        l_x = left_point["x"]
                        l_y = left_point["y"]
                        l_dist = abs(l_x - k) + abs(l_y - j)

                        r_x = right_point["x"]
                        r_y = right_point["y"]
                        r_dist = abs(r_x - k) + abs(r_y - j)

                        if l_dist < r_dist:
                            left_point["x"] = k
                            left_point["y"] = j
                            answer += "L"
                        elif l_dist > r_dist:
                            right_point["x"] = k
                            right_point["y"] = j
                            answer += "R"
                        else:
                            if hand == "left":
                                left_point["x"] = k
                                left_point["y"] = j
                                answer += "L"
                            else:
                                right_point["x"] = k
                                right_point["y"] = j
                                answer += "R"
                            
                    elif num in (1,4,7):
                        left_point["x"] = k
                        left_point["y"] = j
                        answer += "L"
                    elif num in (3,6,9):
                        right_point["x"] = k
                        right_point["y"] = j
                        answer += "R"
    
    return answer