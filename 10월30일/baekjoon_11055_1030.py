N = int(input())

arr = list(map(int,input().split()))

dp = [0]*N
dp[0] = arr[0]

for i in range(1,N) : 
    mx = 0
    for j in range(i) : 
        if arr[i] > arr[j] : 
            mx = max(mx,dp[j]) # i보다 작은 범위에서 최대값을 찾아 거기에 i의 값만더해주면 i
                               # i까지 만들수 있는 값중 최대 값이 만들어진다 
        dp[i] = mx+arr[i]  

print(max(dp))