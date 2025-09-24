from collections import deque 
# S : 시작지점
# E : 출구
# L : 레버
# O : 통로
# X : 벽
def solution(maps) : 
    answer = 0 
    n = len(maps)
    m = len(maps[0])
    visited = [[-1]*m for _ in range(n)]
    lever_distance , lever_x,lever_y = find_lever(maps,visited)
    if lever_distance == -1 : 
        return -1
    else : 
        visited = [[-1]*m for _ in range(n)]

def find_exit(maps,visited) : 
    n = len(maps)
    m = len(maps[0])
    q = deque()
    dx = [0,0,1,-1] 
    dy = [1,-1,0,0]

    q.append()



def find_lever (maps,visited) : 
    if maps[0][0] == "X" : 
        return -1  
    n = len(maps)
    m = len(maps[0])
    q = deque()
    dx = [0,0,1,-1] 
    dy = [1,-1,0,0]

    q.append((0,0))
    visited[0][0] = 0
    while q : 
        x,y = q.popleft()
        for k in range(4) : 
            nx , ny = x+dx[k], y+dy[k]
            if 0<= nx < n and 0<= ny < m  : 
                if maps[nx][ny] in ("O","L") and visited[nx][ny] == -1 : 
                    if maps[nx][ny] == "L" : 
                        return (visited[x][y] +1,nx,ny)
                    else : 
                        visited[nx][ny] = visited[x][y]+1
                        q.append((nx,ny))




    return answer


print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))