# dp 테이블을 만들떄 각 행에 대해서만 생각하고 이전 행과 어떤게 달라지는지 확인해야한다
#이번에는 이전행과 이번행의 최소값을 구하면 되는거다
#내가 틀린이유는 dp테이블을 작성할떄 그 값을 어떤게 넣어야할지 몰랐다 
#dp 를 정의한데로 쎃야한다 중간에 값자기 6이니깐 1원 1개 5원1개해서 그 열에 11 이렇게쓰는게아니라
#2를 적어야한다 
#그래야 규칙이 나온다 

n, k = map (int,input().split())

sset =set()

for _ in range(n) : 
    sset.add(int(input()))

INF = k+1

dp = [INF]*(k+1)
dp[0] = 0

for coin in sset : 
    for j in range(1,k+1) : 
        if j-coin >=0 : 
            dp[j] = min(dp[j],dp[j-coin]+1)

ans = dp[k]

if ans == INF : 
    ans = -1

print(ans)