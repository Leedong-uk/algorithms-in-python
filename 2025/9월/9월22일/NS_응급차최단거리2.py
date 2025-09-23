# 0 -> 통행가능
# 1 -> 통행불가능 
from collections import deque 
def solution(city) : 
    q = deque()
    n = len(city)
    m = len(city[0])
    visited = [[-1]*m for _ in range(n)]
    dx = [0,0,1,-1,1,-1,1,-1] 
    dy = [1,-1,0,0,1,1,-1,-1]

    if city[0][0] != 1 : 

        q.append((0,0))
        visited[0][0] = 1
    else : 
        return -1

    while q : 
        x,y = q.popleft()
        for k in range(8) : 
            nx , ny = x+dx[k],y+dy[k]
            if 0 <= nx < n and 0<= ny < m : 
                if city[nx][ny] == 0 and visited[nx][ny] == -1 : 
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))

    
    return visited[n-1][m-1]


print(solution([[0,0,1,0],[1,0,1,0],[1,0,0,0]]))
