from collections import deque
n , m = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(n)]
check = [[-1]*m for _ in range(n)]
q = deque()
dx = [0,0,-1,1]
dy = [-1,1,0,0]

q.append((0,0))
check[0][0] = 0 

while q : 
    x,y = q.popleft()
    for i in range(4) : 
        nx,ny = x+dx[i] , y+dy[i]
        if 0<= nx <n and 0<=ny<m : 
            if check[nx][ny] == -1 and a[nx][ny] != 0: 
                check[nx][ny] = check[x][y] +1
                q.append((nx,ny))
print(check[n-1][m-1]+1)