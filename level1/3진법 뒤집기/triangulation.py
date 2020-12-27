def solution(n):
    answer = 0
    array = []

    if n == 1:
        array.append(1)
    elif n == 2:
        array.append(2)
    else:
        while True:
            k = int(n % 3)
            n = int(n / 3)

            array.append(k)

            if n < 3:
                array.append(n)
                break

    array.reverse()

    j = 1
    for i in array:
        answer = answer + i * j
        j = j * 3

    return answer