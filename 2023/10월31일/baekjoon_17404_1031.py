N= int(input())

dp = [[0]*3 for _ in range(N)]

for _ in range(N) : 
    arr = list(map(int,input().split()))


for i in range(N) :
    dp[i][0] = max(dp[i-1][1],dp[i-1][2]) + arr[i][0]
    dp[i][1] = max(dp[i-1][0],dp[i-1][2]) + arr[i][1]
    dp[i][2] = max(dp[i-1][0],dp[i-1][1]) + arr[i][2]


print()