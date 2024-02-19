import sys
sys = sys.stdin.readline

N = int(input())
stairs = [0] * 300
for k in range(N):
    stairs[k] = int(input())
    
dp = [0] * 300
dp[0] = stairs[0]
dp[1] = stairs[0]+stairs[1]
dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])

for i in range(3, N):
    dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3], stairs[i]+dp[i-2])

print(dp[N-1])