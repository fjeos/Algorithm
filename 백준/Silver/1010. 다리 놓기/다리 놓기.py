for _ in range(int(input())):
    M, N = map(int, input().split())
    
    temp1, temp2, temp3 = 1, 1, 1
    for i in range(1, N+1):
        temp1 *= i
    
    for j in range(1, (N-M)+1):
        temp2 *= j
        
    for k in range(1, M+1):
        temp3 *= k
        
    print(int(temp1/(temp2*temp3)))