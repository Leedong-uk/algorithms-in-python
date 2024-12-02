#각각의 칸에 물이 언제 차는지 미리 구해놈
#그후 고슴도치가 언제 이동할수있는지 이동시간을 구하고
# 물이 차는 시간보다 이동하는 시간이 작을떄만 이동해서 구해본다

from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n,m = map(int,input().split())
a = [input() for _ in range(n)]
water = [[-1]*m for _ in range(n)]
dist = [[-1]*m for _ in range(n)]

q = deque()
for i in range(n) :
    for j in range(m) : 
        if a[i][j] == "*" :
            q.append((i,j))
            water[i][j] = 0
        if a[i][j] == "S" : 
            sx,sy = i,j
        if a[i][j] == "D" : 
            ex,ey = i,j

#물 count 시작
while q: 
    x,y = q.popleft()
    for k in range(4) : 
        nx , ny = x+dx[k] , y +dy[k]
        if 0<= nx < n and 0<= ny < m : 
            if water[nx][ny] != -1 :
                continue
            if a[nx][ny] in "XD" : 
                continue
            water[nx][ny] = water[x][y] +1
            q.append((nx,ny))

                
dist[sx][sy] = 0
q.append((sx,sy))

while q : 
    x,y =q.popleft()
    for k in range(4) : 
        nx, ny = x +dx[k] , y +dy[k] 
        if 0 <= nx < n and 0<= ny < m : 
            if dist[nx][ny] != -1 : 
                continue
            if a[nx][ny] == "X" : 
                continue
            if  water[nx][ny] != -1 and dist[x][y]+1 >= water[nx][ny] : #여기
                continue
            dist[nx][ny] = dist[x][y]+1
            q.append((nx,ny))

if dist[ex][ey] == -1:
    print('KAKTUS')
else:
    print(dist[ex][ey])