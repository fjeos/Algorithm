def solution(s):
    popped = s.count("0")
    s = s.replace("0", '')
    temp = bin(len(s))
    count = 1

    while len(temp) != 3:
        popped += temp[2:].count("0")
        temp = bin(len(temp[2:].replace("0", '')))

        count += 1
    
    return [count, popped]