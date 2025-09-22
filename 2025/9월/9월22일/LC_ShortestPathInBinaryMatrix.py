from collections import deque 
def shortestPathBinaryMatrix(grid) : 
    dx = [0,0,1,-1,1,1,-1,-1]
    dy = [1,-1,0,0,-1,-1,1,1]
    q = deque()
    n = len(grid)
    m = len(grid[0])
    visited = [[-1]*m for _ in range(n)]

    q.append((0,0))
    visited[0][0] = 0

    while q : 
        x , y = q.popleft()
        for k in range(8) : 
            nx , ny = x+dx[k] , y+dy[k]
            if 0 <= nx < n and 0 <= ny < m : 
                if visited[nx][ny] == -1 and grid[nx][ny] == 0 : 
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
    
    return visited[n-1][m-1]

print(shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))