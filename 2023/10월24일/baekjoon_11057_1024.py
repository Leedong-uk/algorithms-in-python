# dp너무 어렵다 복습해보기!

x= int(input())


dp = [[0]*10 for _ in range(x+1)] 
dp[1] = [1]*10

for i in range(2,x+1) : 
    for j in range(10) : 
        dp[i][j] = sum(dp[i-1][j:])


ans = sum(dp[x])
print(ans%10007)