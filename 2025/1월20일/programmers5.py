from collections import deque
#1은 지나갈수있음 0 은 지나갈수 없음 
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
q = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]
n = len(maps)
m = len(maps[0])

check = [[False]*m for _ in range(n)]
board = [[0]*m for _ in range(n)]

check[0][0] = True
board[0][0] = 1
q.append((0,0))

while q : 
    x ,y = q.popleft()
    for i in range(4) : 
        nx,ny = x+dx[i] , y+dy[i]
        if 0<= nx < n and 0<= ny < m :
            if check[nx][ny] == False  and maps[nx][ny] == 1: 
                check[nx][ny] = True
                board[nx][ny] = board[x][y] +1 
                q.append((nx,ny))
                
result = board[n-1][m-1]

if result == 0 :
    result = -1

print(result)