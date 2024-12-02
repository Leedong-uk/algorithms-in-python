dp =[[0]*3 for _ in range(100001)]

N = int(input())


for _ in range(N) : 
    M = int(input())
    arr = [[0]*(M+1) for _ in range(3)]
  

    for j in range(1,3) : 
        arr[j] = [0]+list(map(int,input().split()))
    
    dp[1][1] = arr[1][1]
    dp[1][2] = arr[2][1]

    for i in range(2,M+1) : 
        dp[i][0] = max(dp[i-1][1],dp[i-1][2])
        dp[i][1] = max(dp[i-1][0],dp[i-1][2]) + arr[1][i]
        dp[i][2] = max(dp[i-1][0],dp[i-1][1]) + arr[2][i]
    

    print(max(dp[M]))




