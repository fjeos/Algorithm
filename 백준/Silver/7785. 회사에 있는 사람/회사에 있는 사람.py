n = int(input())
io = {}
for _ in range(n):
    name, state = input().split()
    io[name] = state

for i in sorted(io.items(), reverse = True):
    if i[1] == 'enter':
        print(i[0])