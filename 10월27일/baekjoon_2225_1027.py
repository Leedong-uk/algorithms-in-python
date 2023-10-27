N , K = map(int,input().split())

dp = [[1]*(N+1) for _ in range(K+1)]

for i in range(2,K+1) : 
    for j in range(1,N+1) : 
        dp[i][j] = dp[i][j-1]+dp[i-1][j]

ans = dp[K][N]
print(ans%1000000000)
