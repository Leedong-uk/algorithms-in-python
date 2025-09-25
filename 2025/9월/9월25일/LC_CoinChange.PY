def coinChange(coins,amount) : 
    dp = [float('inf')]*(amount**2)
    dp[0] = 0
    for coin in coins : 
        dp[coin] = 1 
    
    for i in range(amount+1) : 
        for coin in coins : 
            if i-coin >= 0 : 
                dp[i] = min(dp[i],dp[i-coin]+1)
    
    return dp[amount]
print(coinChange([1,2,5],11))
print(coinChange([2],3))
print(coinChange([1],0))