N, K = map(int, input().split())
lists = list(map(int, input().split()))
lists.sort()
print(lists[K-1])