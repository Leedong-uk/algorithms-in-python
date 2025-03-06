def solution(n):
    answer = 0
    dp = [0]*(n+1)
    
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3,n+1) : 
        dp[i] = dp[i-1] + dp[i-2]
    
    dp[n] = dp[n] if dp[n] < 1000000007 else dp[n] %1000000007
    return answer