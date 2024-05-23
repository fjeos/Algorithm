import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
chats = [input() for _ in range(N)]
users = set()
count = 0
for chat in chats:
    if chat == 'ENTER':
        users.clear()
        continue
    if chat not in users:
        users.add(chat)
        count += 1
print(count)