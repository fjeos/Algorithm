X = int(input())

makdae = 0
gil = 0    
shortest = 0
temp = 64

if X == 64: 
    makdae += 1
    print(makdae)
else:
    while(True) :
        shortest = temp/2
        temp /= 2
        if(shortest <= X):
            if(gil + shortest <= X):
                gil += shortest
                makdae += 1
        if gil == X:
            break
        
    print(makdae)