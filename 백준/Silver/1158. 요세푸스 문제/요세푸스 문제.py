N, K = map(int, input().split())
lists = [i for i in range(N)]
index = -1
result = []

while lists:
    for _ in range(K):
        index += 1
        if index == len(lists):
            index = 0
    result.append(lists.pop(index)+1)
    index -= 1
    
print(f"<{', '.join(map(str, result))}>")