N , K = map(int,input().split())

dp = [1]*(N+1) 
for j in range(2, K+1) : 
    for i in range(1,N+1) : 
        dp[i] = dp[i]+ dp[i-1]

ans = dp[N]

print(ans%1000000000)

