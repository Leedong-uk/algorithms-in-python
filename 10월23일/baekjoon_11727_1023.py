#타일 문제의 핵심은 규칙성을 찾아갈떄앞에 타일을 둔 상태에서 뒤에 붙여가면서 규칙성을 찾아가는것

x = int(input())
dp = [0]*(10001)
dp[1] = 1
dp[2] = 3
for i in range(3,10001) : 
    dp[i] = dp[i-1] + 2*dp[i-2]


y=dp[x]%10007

print(int(y))
