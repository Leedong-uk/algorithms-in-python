from collections import deque
n = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
board = [list(map(int,list(input()))) for _ in range(n)]
village = 0
group  =  [[-1]*n for _ in range(n)]

#단지 구하기 (bfs)
def bfs(start_x,start_y,village) : 
    q = deque()
    q.append((start_x,start_y))
    group[start_x][start_y] = village
    cnt = 1
    while q : 
        x,y = q.popleft()
        for k in range(4) : 
            nx,ny = x+dx[k] , y + dy[k]
            if 0<= nx < n and 0<= ny < n : 
                if board[nx][ny]==1 and group[nx][ny] == -1 : 
                    group[nx][ny] = village
                    q.append((nx,ny))
                    cnt +=1
    return cnt

village_sizes = []
for i in range(n) : 
    for j in range(n) : 
        if board[i][j] == 1 and group[i][j] == -1 : 
            village +=1
            village_sizes.append(bfs(i,j,village))
village_sizes.sort()          
print(len(village_sizes))
for i in village_sizes : 
    print(i)                