lists = [int(input()) for _ in range(3)]
lists.sort()
if lists[0] == lists[1] == lists[2] == 60:
    print("Equilateral")
elif sum(lists) == 180 and (lists[0] == lists[1] or lists[1] == lists[2]):
    print("Isosceles")
elif sum(lists) == 180 and (lists[0] != lists[1] or lists[1] != lists[2]):
    print("Scalene")
else:
    print("Error")