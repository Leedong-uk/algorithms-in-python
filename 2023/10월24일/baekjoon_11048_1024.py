
#드디어 맞췄다 솔직히 쉬운문제였음!
#다만 아쉬운건 맨처음 arr배열을 만들떄 인덱스를 맞춰주기 위해서 페링을 해야하고
#dp테이블도 만들떄 패링을 해야하는데 이떄 N 을써야할지 M 을 써야할지 생각을 해보자 
#또한 for 안에 i 와 j 의 범위는 어떻게 해야하는지도 생각을 해보면 좋을것 같다 

N,M = map(int,input().split())

arr = [[0]*(M+1)]+[[0]+list(map(int, input().split())) for _ in range(N)]
dp =[[0]*(M+1)for _ in range(N+1)]

for i in range(1,N+1) : 
    for j in range(1,M+1) :
        dp[i][j] = max(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+arr[i][j]

print(dp[N][M])