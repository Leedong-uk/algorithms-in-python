#마지막에 최대값 -1
#bfs끝내고  a[][] != -1 이고 group[][] = 0 이라면-1 출력
from collections import deque

m , n = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
q = deque()


def bfs () : 
    while q : 
        x , y = q.popleft()
        cnt = a[x][y]
        for k in range(4) : 
            nx,ny = x+dx[k],y+dy[k]
            if (0<=nx<n) and (0<=ny<m) : 
                if a[nx][ny] == 0 :
                    q.append((nx,ny))
                    a[nx][ny] = cnt+1
    


for i in range(n) : 
    for j in range(m) : 
        if a[i][j] == 1 : 
            q.append((i,j))

bfs()

ans = (max([max(row) for row in a]))-1 # 요것만 알아내면됨 
for i in range(n):
    for j in range(m):
        if a[i][j] == 0 :
            ans = -1

print(ans)




