from collections import deque 
n , m = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(n)]
group  = [[0]*m for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
group[0][0] = 1

def bfs (x,y) : 
    q = deque()
    q.append((x,y))

    while q : 
        x , y = q.popleft()
        cnt = group[x][y]
        for k in range(4) : 
            nx , ny = x+dx[k] , y+dy[k]
            if (0 <= nx < n) and (0 <= ny < m) : 
                if (a[nx][ny] == 1 ) and (group[nx][ny] == 0 ):
                    q.append((nx,ny))
                    group[nx][ny] = cnt + 1


bfs(0,0)
print(group[n-1][m-1])
    