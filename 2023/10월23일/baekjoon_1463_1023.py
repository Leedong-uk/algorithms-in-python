#3으로 최대한 많이 나눠야한다 
"""count = 0
num = int(input())

while num !=1 : 
    if num%3 ==0 :
        num = num //3
        count+=1

    
    elif num%3 == 1 : 
        num = (num-1) //3
        count+=2
        
    
    elif num%2 == 0 : 
        
        num = num//2
        count+=1
        

print(count)
"""

#동적프로그래밍 DP
#dp테이블 안에는 현재 인덱스 값까지 올떄 걸린 연산의 최소값이 들어간다
#dp[i] = dp[i-1]+1 이건 모든 연산에 적용할수있다 그저 전 연산에다가 +1을더한것
#나머지 2의 배수와 3의배수는 단지 곱하기 연산을 한번 하면되기떄문에 그것도 따져줘야한다

x = int(input())

dp=[0]*(x+1)


for i in range(2,x+1): 
    dp[i] = dp[i-1]+1
    if i %2 == 0 : 
        dp[i] = min(dp[i],dp[i//2]+1)
    if i%3 == 0 :
        dp[i] = min(dp[i],dp[i//3]+1)


res = dp[x]
print(res)