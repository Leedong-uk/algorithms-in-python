from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

maps = ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"] 
m = len(maps)
n = len(maps[0])


for i in range(m) : 
    for j in range(n) : 
        if maps[i][j] =="S" : 
            start_x , start_y = i , j 
        elif maps[i][j] == "L" : 
            lever_x , lever_y = i,j
        elif maps[i][j] == "E" : 
            end_x , end_y = i,j
        


def dfs(start_x,start_y,goal_x,goal_y) : 
    check = [[-1]*n for _ in range(m)]
    q = deque()
    check[start_x][start_y] = 0
    q.append((start_x,start_y))
    
    while q: 
        x,y = q.popleft()
        value = check[x][y]
        for k in range(4) :
            nx , ny = x+dx[k] , y+dy[k]
            if (0<= nx < m and 0<=ny < n) : 
                if (check[nx][ny] == -1 and maps[nx][ny]!="X") : 
                    check[nx][ny] = value+1
                    q.append((nx,ny))
    
    return(check[goal_x][goal_y])

lever_distance = dfs(start_x,start_y,lever_x,lever_y)
goal_distance = dfs(lever_x,lever_y,end_x,end_y)

if -1 in (lever_distance, goal_distance):
    print(-1)
else : 
    print(lever_distance+goal_distance)