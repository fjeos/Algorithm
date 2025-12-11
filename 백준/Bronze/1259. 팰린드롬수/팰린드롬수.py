while(True):
    isPel = 1;
    num = list(input())
    if num[0] == '0':
        break;
    n = len(num)
    for i in range(int(n/2)+1):
        if(num[i] != num[n-1-i]):
            isPel = 0
    if isPel == 1:
        print("yes")
    else:
        print("no")