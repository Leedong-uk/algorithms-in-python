from collections import deque
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
shark = {}
answer = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]



            
          
def next_fish (shark) : 
    # 각 fish 에대한 cost 값을 저장할 자료구조 필요
    check = [[-1]*n for _ in range(n)]
    x,y = shark["location"]
    q = deque()
    check[x][y] = 0
    q.append((x,y))
    candidates=[]
    
    while q : 
        x,y = q.popleft()
        for k in range(4) : 
            nx , ny = x+dx[k] , y+dy[k]
            if (0<= nx < n and 0<= ny < n) : 
                if check[nx][ny] == -1 and board[nx][ny] == 0 : 
                    go = False
                    eat = False 
                    
                    if board[nx][ny] == 0 : 
                        go = True
                    elif board[nx][ny] < shark["size"] : 
                        go = True
                        eat = True
                    elif board[nx][ny] == shark["size"] : 
                        go = True
                    
                    if go : 
                        q.append((nx,ny))
                        check[nx][ny] = check[x][y]+1
                        if eat : 
                            candidates.append((check[nx][ny],nx,ny))
    if not candidates : 
        return None
    candidates.sort()
    return candidates[0]


for i in range(n) : 
    for j in range(n) : 
        if board[i][j] == 9 : 
            shark["location"] = (i,j)
            shark["count"] = 0
            shark["size"] = 2
            board[i][j] = 0
            
            while True : 
                info = next_fish(shark)
                if info is None : 
                    break
                time , nx,ny = info
                
                shark["location"] = (nx, ny)
                board[nx][ny] = 0
                answer += time
                shark["count"] +=1
                
                if shark["size"] == shark["count"] : 
                    shark["size"] +=1
                    shark["count"] = 0
                
                
                            
   
    
                