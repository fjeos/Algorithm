import sys

input = lambda: sys.stdin.readline().rstrip()
first_dic = {1: 500, 3: 300, 6: 200, 10: 50, 15: 30, 21: 10}
second_dic = {1: 512, 3: 256, 7: 128, 15: 64, 31: 32}
for _ in range(int(input())):
    a, b = map(int, input().split())
    first_prize, second_prize = 0, 0
    if a != 0:
        for i in first_dic.keys():
            if a <= i:
                first_prize = first_dic[i]
                break
    if b != 0:
        for j in second_dic.keys():
            if b <= j:
                second_prize = second_dic[j]
                break
    print((first_prize + second_prize) * 10000)
