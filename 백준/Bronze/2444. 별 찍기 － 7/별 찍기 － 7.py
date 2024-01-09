N = int(input())
star = 1
for i in range(N):
    for j in range(i, N-1):
        print(" ", end='')
    for k in range(star):
        print("*", end='')
    print("\n", end='')
    if i!=N-1:
        star+=2
    
star-=2
for i in range(N-1, 0, -1):
    for j in range(N-i):
         print(" ", end='')
    for k in range(star):
        print("*", end='')
    if N != 0:
        print("\n", end='')
    star-=2
