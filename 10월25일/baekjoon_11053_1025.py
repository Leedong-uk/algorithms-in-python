#이번 문제를 혼자 못풀었던이유
#처음에 생각이 굉장히 비슷했는데 나는 here 이라는 변수를 줘서
#기준을 잡을려고했다 구현하려고하다보니 here도 계속 증가해야한다고 생각했다
# 설명을 보니 here 도 계속 갱신되어야하기떄문에
#그냥i와 j를 줘서 2중 for문을 만들면 된다는 점을 알았다 


N = int(input())
for i in range(N) : 
    a = [0]+list(map(int,input().split()))


dp = [0]*(N+1)

for i in range(1, N+1):
    mx = 0
    for j in range(0, i):   
        if lst[i]>lst[j]:
            mx = max(mx, dp[j])
    dp[i] = mx+1


print(max(dp))