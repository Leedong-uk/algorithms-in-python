N = int(input())

lst = list(map(int,input().split()))
dp = [1]*N

for i in range(1,N):
    mx = 0
    for j in range(i): 
        if lst[i] < lst[j] : 
            mx = max(mx,dp[j])
        dp[i] = mx +1

print(max(dp))  

