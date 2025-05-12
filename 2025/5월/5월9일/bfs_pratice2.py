from collections import deque
dx = [0,0,1,-1,1,-1,1,-1]
dy = [1,-1,0,0,1,1,-1,-1]

city = [
    [1, 0, 0, 0],
    [1, 1, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 0]
]

m = len(city) # 행
n = len(city[0]) #열
check = [[-1] * n for _ in range(m)]
q = deque()

check[0][0] = 1
q.append((0,0))

while q: 
    x,y = q.popleft()
    value = check[x][y]
    for k in range(8) : 
        nx , ny = x+dx[k],y+dy[k]
        if (0<= nx < m and 0<=ny < n) : 
            if(city[nx][ny] == 0 and check[nx][ny] == -1):
                check[nx][ny] = value+1
                q.append((nx,ny))
                
print(check[m-1][n-1])

