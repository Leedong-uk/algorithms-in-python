from collections import deque
def solution(maps):
    answer = 0 
    n = len(maps) 
    m = len(maps[0])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    for i in range(n) :
        for j in range(m) : 
            if maps[i][j] == "S" :
                start_x,start_y = i,j
            elif maps[i][j] == "L" : 
                lever_x,lever_y = i,j
            elif maps[i][j] == "E" : 
                end_x,end_y = i,j    
                    
    
    def bfs(start_x,start_y,goal_x,goal_y) : 
        check = [[-1]*m for _ in range(n)]
        q = deque()
        
        check[start_x][start_y] = 0 
        q.append((start_x,start_y))
        
        while q : 
            x,y = q.popleft()
            value = check[x][y]
            for k in range(4) : 
                nx , ny = x+dx[k] , y+dy[k]
                if (0<= nx < n and 0<= ny < m) : 
                    if check[nx][ny] == -1 and maps[nx][ny] != "X" : 
                        check[nx][ny] = value+1 
                        q.append((nx,ny))
        
        return check[goal_x][goal_y]
    
    lever_distance = bfs(start_x,start_y,lever_x,lever_y)
    goal_distance = bfs(lever_x,lever_y,end_x,end_y)
    
    if lever_distance == -1 or goal_distance == -1 : 
        return -1 
    else : 
        answer = lever_distance+goal_distance
        
    
    return answer

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))