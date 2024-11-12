import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    days = int(input())
    stocks = list(map(int, input().split()))
    max_value = max(stocks)  # 일수 중의 최대 주가

    profit = 0  # 주식으로 번 돈, answer
    spent = 0  # 주식을 사는 데 쓴 돈
    my_stock = 0  # 현재 보유중인 주

    for i in range(days):
        if i == days - 1 and stocks[i] > stocks[i - 1]:
            profit += (stocks[i] * my_stock) - spent
            break
        elif stocks[i] != max_value:
            spent += stocks[i]
            my_stock += 1
        else:
            profit += (stocks[i] * my_stock) - spent
            my_stock = 0
            spent = 0
            is_descending = True
            for j in range(i + 1, days - 1):
                if stocks[j] < stocks[j + 1]:
                    is_descending = False
            if is_descending:
                break
            else:
                max_value = max(stocks[i + 1:]) if i != days - 1 else stocks[-1]
    print(profit)
