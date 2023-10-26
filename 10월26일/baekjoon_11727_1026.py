N= int(input())
dp = [0]*(10001)
dp[1] = 1
dp[2] = 3

for i in range(3,N+1) : 
    dp[i] = dp[i-1] + 2*dp[i-2]

x = dp[N]
print(x%10007)