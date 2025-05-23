from collections import deque
n = 4
m = 4 
hole = [[2, 3], [3, 3]]
board = [[-1]*n for _ in range(m)]
check = [[[-1]*2 for _ in range(n)]for _ in range(m)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
jump_x = [0, 0, 2, -2]
jump_y = [2, -2, 0, 0]
q = deque()

for hole_pos in hole : 
    x,y = hole_pos
    board[x-1][y-1] = -2

check[0][0][1] = 0
q.append((0,0,1))

while q: 
    x,y,z = q.popleft()
    value = check[x][y][z]
    for k in range(4) : 
        nx,ny = x+dx[k] , y+dy[k]
        if (0<= nx < m and 0<= ny < n ) : 
            if check[nx][ny][z] == -1 and board[nx][ny] == -1 : 
                check[nx][ny][z] = value+1
                q.append((nx,ny,z))
    
    if z == 1 : 
        for k in range(4) : 
            jx, jy = x + jump_x[k], y + jump_y[k]
            if 0 <= jx < m and 0 <= jy < n  : 
                if check[jx][jy][0] == -1 and board[jx][jy] == -1 :
                    check[jx][jy][0] = value+1
                    q.append((jx,jy,0))
        

val1 = check[m-1][n-1][0]
val2 = check[m-1][n-1][1]


if val1 >= 0 and val2 >= 0:
    result = min(val1, val2)
elif val1 >= 0:
    result = val1
elif val2 >= 0:
    result = val2
print(result)
            
            
        