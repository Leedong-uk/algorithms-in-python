from collections import deque
n = 3
start = 0
cnt = 0
q=deque()
check = [False] * (2001)
check[start] = True 
q.append(start)

while q :
    x = q.popleft()

    if x == n :
        cnt +=1


    if x+1 <= n and check[x+1] == False : 
        q.append(x+1)
    
    if x+2 <= n and check[x+2] == False : 
        q.append(x+2)
    

print(cnt)

# dp로 풀기
def solution(n):
    MOD = 1234567  

    # DP 배열 초기화
    dp = [0] * (n + 1)
    dp[1] = 1  # 1칸에 도달하는 방법: 1가지
    if n >= 2:
        dp[2] = 2  # 2칸에 도달하는 방법: 2가지

    # 점화식으로 DP 배열 채우기
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

    return dp[n]