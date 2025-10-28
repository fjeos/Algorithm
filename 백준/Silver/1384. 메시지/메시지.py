i = 1
while(True):
    include =  False
    N = int(input())
    if N == 0:
        break;
    group = [input().split() for _ in range(N)]
    print("Group {0}".format(i))
    
    for col in group:
        if 'N' in col:
            include = True

    if include == False:
        print("Nobody was nasty")
    else:
        for j in range(N):
            for k in range(N):
                if group[j][k] == 'N':
                    print("{0} was nasty about {1}".format(group[j-k][0], group[j][0]))

    i += 1
    print()