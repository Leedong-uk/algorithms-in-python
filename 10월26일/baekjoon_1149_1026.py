N = int(input())
lst = [0]+[int(input()) for _ in range(N)]


dp = [[0]*3 for _ in range(N+1)]
for i in range(1, N+1):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2])  
    dp[i][1] = dp[i-1][0]+lst[i]            
    dp[i][2] = dp[i-1][1]+lst[i]            

print(max(dp[N][1:3]))