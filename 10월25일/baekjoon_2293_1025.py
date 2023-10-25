#이전 문제와 매우 유사했음
#일단 다 적어보고 그다음에 규칙을 찾아!

N, K = map (int,input().split())

lst = [int(input()) for _ in range(N)]


dp = [0]*(K+1)
dp[0] = 1


for coin in lst : 
   
    for j in range(K+1):
        if j-coin >= 0 :
            dp[j] = dp[j]+dp[j-coin]


print(dp[K])