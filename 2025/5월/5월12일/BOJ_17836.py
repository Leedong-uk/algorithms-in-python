from collections import deque
n,m,t = map(int,input().split())
dx = [0,0,1,-1]
dy = [1,-1,0,0]
board = [list(map(int,input().split())) for _ in range(n)]


def bfs() : 
    check = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0, 0, 0))  
    check[0][0][0] = 0
    
    while q : 
        x,y,z = q.popleft()
        value = check[x][y][z]
        
        if (x,y) == (n-1,m-1) : 
            return check[x][y][z]
        
        for k in range(4) : 
            nx,ny,nz = x+dx[k], y+dy[k] , z
            if (0<= nx < n  and 0<=ny<m) : 
                #검을 가지고 벽을 만난 경우 
                if board[nx][ny] == 1 and check[nx][ny][nz] == -1 and nz == 1:
                        check[nx][ny][1] = value +1
                        q.append((nx,ny,1))
                
                #방문 안한 통로를 만난 경우
                if board[nx][ny] ==0 and check[nx][ny][nz] == -1 : 
                    check[nx][ny][nz] = value+1
                    q.append((nx,ny,nz))
                
                #방문 안한 검을 만난 경우
                if board[nx][ny] ==2 and check[nx][ny][nz] == -1 : 
                    check[nx][ny][1] = value+1
                    q.append((nx,ny,1))
    return float('inf') 
result = bfs()

if result <=t : 
    print(result)
else : 
    print("Fail")