from collections import deque
# board =  n x n / m명의 승객 / gas
n , m , gas = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
car_x , car_y = map(int,input().split())
person = []
goal = [] 
person_distance=[]
check = [[False]*n for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(m) : 
    p_x,p_y,g_x,g_y = map(int,input().split())
    person.append([(p_x,p_y),(g_x,g_y)])


def bfs(start_x,start_y,goal_x,goal_y) : 
    check[start_x][start_y] = True
    q = deque()
    q.append((start_x,start_y))
    
    while q : 
        x,y = q.popleft()
        
        for k in range(4) : 
            nx,ny = x+dx[k] , y+dy[k]
            
            if(0<= nx < n and 0<=ny < n) : 
                if check[nx][ny] == False :
                    check[nx][ny] = True
                    q.append((nx,ny))


        