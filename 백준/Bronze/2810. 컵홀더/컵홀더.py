N = int(input())
seat = list(input())
i = 0
seat.insert(0, '*')
while(True):
    if seat[i] == 'S':
        seat.insert(i+1, '*')
    elif seat[i] == 'L' and seat[i-1] == 'L':
        seat.insert(i+1, '*')
    i += 1
    if seat[len(seat)-1] == '*':
        break
if N <= 3:
    print(N)
else:
    print(seat.count('*'))    