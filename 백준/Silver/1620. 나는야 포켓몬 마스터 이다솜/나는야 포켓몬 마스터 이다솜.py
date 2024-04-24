import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
name_dic, digit_dic = {}, {}

for i in range(1, N+1):
    name_dic[input()] = i
for key, value in name_dic.items():
    digit_dic[value] = key

for _ in range(M):
    quiz = input()
    if quiz.isdigit():
        print(digit_dic[int(quiz)])
    else:
        print(name_dic[quiz])
