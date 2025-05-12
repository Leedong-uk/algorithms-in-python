from collections import deque
dx = [0,0,1,-1,1,-1,1,-1]
dy = [1,-1,0,0,1,1,-1,-1]
grid = [[1,0,0],[1,1,0],[1,1,0]]

n = len(grid) # 행
m  = len(grid[0])  # 열

check = [[-1]*m for _ in range(m)]
q = deque()

check[0][0] = 1
q.append((0,0))

while q : 
    x,y = q.popleft()
    value = check[x][y] 
    
    for k in range(8):
        nx,ny = x+dx[k] , y+dy[k]
        
        if (0<=nx < n and 0<= ny < m) : 
            if (grid[nx][ny] == 0 and check[nx][ny] == -1 ) : 
                check[nx][ny] = value+1
                q.append((nx,ny))
print(check[n-1][m-1])
