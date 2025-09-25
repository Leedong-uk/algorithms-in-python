# 0 : 벽
# 1 : 통로 
from collections import deque
def solution(maps) : 
    answer = 0 
    q = deque()
    n = len(maps)
    m = len(maps[0])
    visited = [[-1]*m for _ in range(n)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q.append((0,0))
    visited[0][0] = 1

    while q: 
        x,y = q.popleft()
        for k in range(4) : 
            nx,ny = x+dx[k] , y+dy[k]
            if 0<= nx < n and 0 <= ny < m : 
                if maps[nx][ny] == 1 and visited[nx][ny] == -1 : 
                    visited[nx][ny] = visited[x][y]+1
                    q.append((nx,ny))
    
    answer = visited[n-1][m-1]

    return answer 

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))