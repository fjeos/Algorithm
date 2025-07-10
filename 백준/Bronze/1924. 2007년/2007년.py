x, y = map(int, input().split())
month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
date = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
days = 0

for i in range(1, x):
    days += month[i]
days += y

print(date[days%7])