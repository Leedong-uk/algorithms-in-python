x = int(input())
dp = [0]*(x+1)
x1,x2,x3,x4 = map(int,input().split())

dp[1] =x1
dp[2] = max(2*x1,x2)
dp[3] = max(x1+dp[2],x2+x1,x3)

for i in range(4,x+1) : 
    dp[i] = max(x1+dp[i-1],x2+dp[x-2],x3+dp[x-3],x4+dp[x-4])


print(dp[x])

#dp가 부족한거 같아서 내일은  dp 필수문제 요걸 풀어보겠습니다
