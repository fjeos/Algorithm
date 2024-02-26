import sys
input = sys.stdin.readline

N, M = map(int, input().split())
price = [list(map(int, input().split())) for _ in range(M)]
result = 0
natMin = 99999
packMin = 99999
for i in range(M):
    if price[i][0] < packMin:
        packMin = price[i][0]
    if price[i][1] < natMin:
        natMin = price[i][1]
while N > 0:
    if N >= 6:   
        result += (packMin if packMin < natMin * 6 else natMin * 6)
        N -= 6
    else:
        result += (packMin if packMin < natMin * N else natMin * N)
        N -= N
        
print(result)