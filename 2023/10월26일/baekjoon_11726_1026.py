x = int(input())

dp = [0]*(x+1)
dp[1]=1
dp[2]=2

for i in range(3,x+1) : 
    dp[i] = dp[i-1]+dp[i-2]

y= dp[x]

print(int(y%10007))


