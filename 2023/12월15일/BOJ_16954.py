#8개의 미로를 다 만들 필요없고
#t 초후 도착한 칸이 벽인지
#t+1 (이동한후 1초후)에 벽이 내려오는지 아닌지만 확인하면 된다 
#이 문제는 이동하고 벽이 내려오기떄문에 만일 내가 3,4에 이미 도착했는데 벽이 내려온다면?
#깔린다 안된다는소리임
from collections import deque
dx = [0,0,1,-1,1,-1,1,-1,0]
dy = [1,-1,0,0,1,1,-1,-1,0]
n = 8
a = [input() for _ in range(n)]
q = deque()
check = [[[False]*(n+1) for j in range(n)] for i in range(n)]
check[7][0][0] = True
q.append((7,0,0))
ans = False

while q:
    x,y,t = q.popleft()
    if x == 0 and y == 7:
        ans = True
    for k in range(9):
        nx,ny = x+dx[k],y+dy[k]
        nt = min(t+1, 8)
        if 0 <= nx < n and 0 <= ny < n:
            if nx-t >= 0 and a[nx-t][ny] == '#':
                continue
            if nx-t-1 >= 0 and a[nx-t-1][ny] == '#':
                continue
            if check[nx][ny][nt] == False:
                check[nx][ny][nt] = True
                q.append((nx,ny,nt))

print(1 if ans else 0)


