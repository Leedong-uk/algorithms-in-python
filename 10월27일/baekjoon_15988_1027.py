
dp = [0 for i in range(1000001)]
dp[0]=1
dp[1]=1
dp[2]=2

for i in range(3, 1000001):
    dp[i] = dp[i-3]%1000000009+dp[i-2]%1000000009+dp[i-1]%1000000009

N = int(input())
for _ in range(N) : 
    M = int(input())
    print(dp[M]%1000000009)