N = int(input())
trees = list(map(int, input().split()))
trees.sort(reverse = True)
print(max(map(lambda x, y: x+y+2, trees, range(N))))