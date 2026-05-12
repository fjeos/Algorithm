def solution(number, limit, power):
    answer = 0
    counts = []
    count = 0
    for el in range(1, number+1):
        for i in range(1, int(el**0.5) + 1):
            if el % i == 0:
                if i * i == el:
                    count += 1
                else:
                    count += 2 
        counts.append(count)
        count = 0
        
    for j in range(number):
        if counts[j] > limit:
            counts[j] = power
    
    return sum(counts)