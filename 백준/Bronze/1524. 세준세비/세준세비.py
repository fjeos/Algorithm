for _ in range(int(input())):
    input()
    temp = []
    N, M = map(int, input().split())
    list1 = list(map(int, input().split()))
    list1.sort()
    list2 = list(map(int, input().split()))
    list2.sort()
    while(True):        
        if list1[0] < list2[0]:
            del list1[0]
        elif list1[0] >= list2[0]:
            del list2[0]
        if not list1:
            break;
        elif not list2:
            break;
    if list1:
        print("S")
    else:
        print("B")