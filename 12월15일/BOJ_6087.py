from collections import deque
m , n = map(int,input().split())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

a = [input() for _ in range(n)]
d = [[-1]*m for _ in range(n)]
razar = []

for i in range(n) : 
    for j in range(m) :
        if a[i][j] == "C" :
            razar.append((i,j))

sx,sy = razar[0]
ex,ey = razar[1]

q = deque()
q.append((sx,sy))
d[sx][sy] = 0 

while q : 
    x,y = q.popleft()
    for k in range(4) : 
        nx,ny = x+dx[k], y+dy[k]
        while 0<= nx < n and 0<= ny < m :
            if a[nx][ny] == '*' : 
                break
            if d[nx][ny] == -1 : 
                d[nx][ny] = d[x][y] + 1
                q.append((nx,ny))
            
            nx +=dx[k]
            ny +=dy[k]

print(d[ex][ey]-1)





