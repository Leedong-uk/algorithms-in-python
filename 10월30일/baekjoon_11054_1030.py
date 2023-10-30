#바이토닉 수열 
#일단 우리가 기존에 구하는 방식으로 가장 긴 증가하는 수열을 구해준다
#그후 수열을 거꾸로하고 거꾸로 출력하면서 가장 긴 증가하는 수열을 구해주면 그게 감소하는 수열이다
#그후 그 배열의 각 index값에 있는 값들을 더해주고 거기에 -1 한 값중 가장 큰값이 바이토닉 수열에 가장 긴 부분이다

N = int(input())

arr = list(map(int,input().split()))
i_dp = [1]*N
d_dp = [1]*N
result = [0]*N
ans = 0


for i in range(1,N) : 
    mx = 0
    for j in range(i) : 
        if arr[i] > arr[j] : 
            mx = max(mx,i_dp[j]) 
                                
        i_dp[i] = mx+1 


arr.reverse()
for i in range(1,N) : 
    mx = 0
    for j in range(i) : 
        if arr[i] > arr[j] : 
            mx = max(mx,d_dp[j]) 
                               
        d_dp[i] = mx+1 
d_dp.reverse()

for i in range(N) : 
    result[i] = i_dp[i] +d_dp[i] -1

print(max(result))