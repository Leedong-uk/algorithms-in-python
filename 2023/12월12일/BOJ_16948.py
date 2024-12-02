from collections import deque
n = int(input())
start_x , start_y , goal_x , goal_y = map(int,input().split())

dx=[-2,-2,0,0,2,2]
dy=[-1,1,-2,2,-1,1]

q = deque()
dist = [[-1]*n for _ in range(n)] #방문안했으면 -1 방문했으면 

q.append((start_x,start_y))
dist[start_x][start_y] = 0 

while q : 
    x , y = q.popleft()
    for k in range(6) : 
        nx , ny = x+dx[k], y+dy[k]

        if 0<= nx < n and 0<= ny < n :
            if dist[nx][ny] == -1 :
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))

print(dist[goal_x][goal_y])



