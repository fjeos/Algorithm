def gcd(array):
    result = array[0]
    for i in range(len(array) - 1):
        a, b = result, array[i + 1]
        while b != 0:
            r = a % b
            a = b
            b = r
        result = a
    return result


def solution(arrayA, arrayB):
    answer = 0
    cd = gcd(arrayA)
    cant_divide = True
    for num in arrayB:
        if num % cd == 0:
            cant_divide = False
    if cant_divide:
        answer = cd

    cd = gcd(arrayB)
    cant_divide = True
    for num in arrayA:
        if num % cd == 0:
            cant_divide = False
    if cant_divide:
        answer = max(answer, cd)
    return answer
