import sys
input = lambda: sys.stdin.readline().rstrip()

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

count, i = 1, 1
total_weight = trucks[0]
bridge = [[trucks[0], w - 1]]
while bridge:
    if bridge[0][1] == 0:
        total_weight -= bridge[0][0]
        bridge.pop(0)
    for j in range(len(bridge)):
        bridge[j][1] -= 1
    if n != 1 and i < n and total_weight + trucks[i] <= L:
        bridge.append([trucks[i], w - 1])
        total_weight += trucks[i]
        i += 1
    count += 1

print(count)