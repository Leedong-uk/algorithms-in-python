from collections import deque

n = 4
m = 4
hole = [[2, 3], [3, 3]]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
jump_x = [0, 0, 2, -2]
jump_y = [2, -2, 0, 0]


check = [[[0] * 2 for _ in range(m)] for _ in range(n)]


for x, y in hole:
    check[x-1][y-1][0] = -1
    check[x-1][y-1][1] = -1


q = deque()
check[0][0][1] = 0  
q.append((0, 0, 1))  

while q:
    x, y, z = q.popleft()
    value = check[x][y][z]

   
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if check[nx][ny][z] == 0:  
                check[nx][ny][z] = value + 1
                q.append((nx, ny, z))

    if z == 1:  
        for k in range(4):
            jx, jy = x + jump_x[k], y + jump_y[k]
            if 0 <= jx < n and 0 <= jy < m:
                if check[jx][jy][0] == 0: 
                    check[jx][jy][0] = value + 1  
                    q.append((jx, jy, 0)) 

result = min(check[n-1][m-1])  
print(result)

