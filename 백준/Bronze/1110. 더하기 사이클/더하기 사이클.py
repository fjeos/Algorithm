N = list(input())
list1 = N.copy()
cycle = 0
list2 = [0, 0]

if len(list1) == 1:
    list1.insert(0, '0')
    N.insert(0, '0')
    
while(True):
    num = int(list1[0]) + int(list1[1])
    list2[0] = (list1[1])
    list2[1] = (str(num%10))
    list1 = list2
    cycle += 1
    if list1[0] == N[0] and list1[1] == N[1] : 
        break    
print(cycle)