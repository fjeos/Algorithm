global dp0
global dp1
    
def fibo(n): 
    if n == 0 or n == 1:
        return
    for i in range(1, n):
        dp0.append(dp0[i]+dp0[i-1])
        dp1.append(dp1[i]+dp1[i-1])

T = int(input())
for _ in range(T):
    N = int(input())
    dp0 = [1, 0]
    dp1 = [0, 1]
    fibo(N)
    print(dp0[N], dp1[N])