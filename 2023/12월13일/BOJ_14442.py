#이거 그거네 가중치가 1과 0 인 bfs
#덱을 이용해서 가중치가 0이면 앞에 붙이고 가중치가 1이면 뒤에 붙여서 bfs실행
#아니 그건 가중치가 달라진거고 이건 정점 나누기잖아 
#그냥 맨처음 문제가 1번의 제한 조건이 주어졌다면 여기는 K개의 제한조건이 들어감


from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n,m,l = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(n)]
d = [[[0]*11 for i in range(m)] for j in range(n)]
q = deque()
d[0][0][0] = 1
q.append((0,0,0))

while q:
    x,y,z = q.popleft()
    for k in range(4):
        nx,ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m :
            if a[nx][ny] == 0 and d[nx][ny][z] == 0:
                d[nx][ny][z] = d[x][y][z] + 1
                q.append((nx,ny,z))

            if z+1 <= l and a[nx][ny] == 1 and d[nx][ny][z+1] == 0:
                d[nx][ny][z+1] = d[x][y][z] + 1
                q.append((nx,ny,z+1))
ans = -1
for i in range(l+1) : 
    if d[n-1][m-1][i] == 0 : 
        continue
    if ans == -1 or d[n-1][m-1][i] < ans : 
        ans = d[n-1][m-1][i]
print(ans)
