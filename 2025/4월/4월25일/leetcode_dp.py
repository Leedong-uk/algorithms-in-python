coins = [1,2,5]
amount = 11
inf_value = float('inf')
dp = [inf_value] *(amount+1)
dp[0]=0

for i in coins : 
    dp[i] = i

for i in range(amount+1) : 
    for coin in coins : 
        if i >=coin : 
            dp[i] = min(dp[i],dp[i-coin]+1)
print(dp[amount])