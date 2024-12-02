import sys
input = sys.stdin.readline

n , m = map(int,input().split())
a = [list(map(lambda x:ord(x)-65, input())) for _ in range(n)]
dx = [0,-1,0,1]
dy = [1,0,-1,0]
max_ = 1
check = [False] *26




def dfs(x,y,cnt) : 
    global max_
    max_ = max(max_,cnt)
    
    for k in range(4) : 
        nx,ny = x+dx[k] , y + dy[k]

        if 0 <= nx < n and 0 <= ny < m :
            if check[a[nx][ny]] == False : 
                check[a[nx][ny]] = True
                dfs(nx,ny,cnt+1)
                check[a[nx][ny]] = False

check[a[0][0]] = True
dfs(0,0,max_)
print(max_)
