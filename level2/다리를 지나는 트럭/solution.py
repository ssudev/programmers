def solution(bridge_length, weight, truck_weights):
    answer = 0 
    bridge_array = [0]*(bridge_length+1)
    truck = truck_weights[0]
    truck_length = len(truck_weights)
    all_weights = 0
    cnt = 0
    
    while True:
        bridge_array.insert(0,0)    
        bridge_array = bridge_array[0:bridge_length+1]
        
        if bridge_array[bridge_length] != 0:
            all_weights -= bridge_array[bridge_length]
            bridge_array[bridge_length] = 0
            
        if truck_length > 0:
            truck = truck_weights[0]
            
        # 합보다 작은 경우
        if all_weights + truck <= weight and truck_length > 0:
            truck = truck_weights.pop(0)
            bridge_array[0] = truck    
            all_weights += truck
            truck_length -= 1

        cnt += 1
           
        if truck_length == 0 and all_weights == 0:
            break
    
    answer = cnt

    return answer