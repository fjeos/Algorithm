def solution(n):
    answer = []
    binary = bin(n).replace("0b", "")
    ones = binary.count('1')
    i = n + 1
    while True:
        next_binary = bin(i).replace("0b", "")
        one = next_binary.count('1')
        if one == ones:
            return i
        i += 1
        