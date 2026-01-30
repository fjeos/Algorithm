N = int(input())
lists = [input() for _ in range(N)]
    
if lists == sorted(lists) :
    print("INCREASING")
elif lists == sorted(lists, reverse = True):
    print("DECREASING")
else:
    print("NEITHER")