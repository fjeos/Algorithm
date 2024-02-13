S = int(input())
count, summ = 0, 0

while summ <= S:
    summ += count
    count += 1

print(count-2)