from collections import deque 
n , m = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(n)]
group  = [[0]*m for _ in range(n)]
q = deque()

dx = [0,0,1,-1]
dy = [1,-1,0,0]

group[0][0] = 1
q.append((0,0))

while q : 
    x ,y = q.popleft()
    cnt = group[x][y]
    for k in range(4) : 
        nx , ny = dx[k] +x , dy[k]+y
        if (0 <= nx < n) and (0 <= ny < m) : 
            if a[nx][ny] == 1 and group[nx][ny] == 0 : 
                group[nx][ny] = cnt + 1
                q.append((nx,ny))

print(group[n-1][m-1])