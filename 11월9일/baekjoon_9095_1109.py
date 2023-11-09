
#solution by DP
n = int(input())
def dp(x) : 
    dp = [0]*(x+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4,n+1) : 
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    
    return dp[n]

for _ in range (n) : 
    x = int(input())
    print(dp(x))
