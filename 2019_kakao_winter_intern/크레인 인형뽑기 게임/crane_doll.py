def solution(board, moves):
    board2 = [[0 for col in range(len(board[0]))] for row in range(len(board))]
    answer = 0
    array = []
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            board2[i][j] = board[j][i]

    for k in moves:
        for i in board2[k-1:k]:
            for idx, j in enumerate(i):
                if j != 0:
                    array.append(j)
                    board2[k-1][idx] = 0
                    break
    
    if array == []:
        return answer
    
    i = 1
    while True:

        if array[i-1] == array[i]:
            answer += 2
            print(array[i-1], array[i])
            array.pop(i-1)
            array.pop(i-1)
            i -= 1
        else:
            i += 1

        if i >= len(array):
            break
    
        if len(array) <= 1:
            break

            
    return answer