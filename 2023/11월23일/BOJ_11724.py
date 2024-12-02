import sys
sys.setrecursionlimit(100000) 
#재귀를 사용해서 문제를 풀려면 이코드는 필수다
#파이썬의 기본 재귀 깊이 제한은 1000으로 매우 얕은편이다
#따라서 재귀로 문제를 풀경우 드물지 않게 이 제한에 걸리게 된다 이걸 넣어서 제한을 깊이 만들어 줘야한다

n,m =map(int,input().split())
a = [[] for _ in range(n+1)] #인접리스트 
check = [False] *(n+1)
cnt = 0

#인접리스트 만들기 
for _ in range(m) : 
    u , v = map(int,input().split())
    a[u].append(v)
    a[v].append(u)


#dfs
def dfs(x) : 
    check[x] = True 
    for i in a[x] : 
        if check[i] == False :
            dfs(i)


for i in range(1,n+1) : 
    if check[i] == False :
        dfs(i)
        cnt +=1


print(cnt)


