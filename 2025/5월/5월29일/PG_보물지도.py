from collections import deque

def solution(n, m, hole):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    jump_x = [0, 0, 2, -2]
    jump_y = [2, -2, 0, 0]
    
    check = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
    
    for x, y in hole:
        check[x-1][y-1][0] = -2  
        check[x-1][y-1][1] = -2  
    
    q = deque()
    check[0][0][1] = 0  
    q.append((0, 0, 1))  
    
    while q:
        x, y, z = q.popleft()
        value = check[x][y][z]
        
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and check[nx][ny][z] == -1:
                check[nx][ny][z] = value + 1
                q.append((nx, ny, z))
        
        if z == 1:
            for k in range(4):
                jx, jy = x + jump_x[k], y + jump_y[k]
                if 0 <= jx < n and 0 <= jy < m and check[jx][jy][0] == -1:
                    check[jx][jy][0] = value + 1
                    q.append((jx, jy, 0))
    a = check[n-1][m-1][0]
    b = check[n-1][m-1][1]
    
    result = -1
    if a >= 0 and b >= 0:
        result = min(a, b)
    elif a >= 0:
        result = a
    elif b >= 0:
        result = b
    
    return result
