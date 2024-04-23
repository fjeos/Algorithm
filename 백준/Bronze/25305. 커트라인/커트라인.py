N, K = map(int, input().split())
print(sorted(list(map(int, input().split())), reverse=True)[K-1])