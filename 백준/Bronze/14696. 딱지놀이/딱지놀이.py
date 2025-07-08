result = []
for _ in range(int(input())):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    del(A[0])
    del(B[0])
    countA = []
    countB = []
    
    for i in range(4, 0, -1):
        countA.append(A.count(i))
    for i in range(4, 0, -1):
        countB.append(B.count(i))
    
    if countA[0] > countB[0]:
        result.append('A')
    elif countA[0] == countB[0]:
        if countA[1] > countB[1]:
            result.append('A')
        elif countA[1] == countB[1]:
            if countA[2] > countB[2]:
                result.append('A')
            elif countA[2] == countB[2]:
                if countA[3] > countB[3]:
                    result.append('A')
                elif countA[3] == countB[3]:
                    if countA[3] > countA[3]:
                        result.append('A')
                    elif countA[3] == countB[3]:
                        result.append('D')
                    else:
                        result.append('B')
                else:
                    result.append('B')
            else:
                result.append('B')
        else:
             result.append('B')
    else:
        result.append('B')
print('\n'.join(map(str, result)))