# 0 : 바다 1 : 육지
#a = 가장 처음에 각 섬에 대해서 그룹을 짓는다 1번섬 , 2번섬 ,3번섬
#group = 각섬의 모든점에서 섬까지의 거리를 구한다 그럼 섬 안에있 는 육지는 모두 거리가 0이된다
#그후 각각의 정점이 모두 거리가 1인곳을 방문한다 이러는동시에 섬이 확장된다는 식으로 a의 집합 1 ,2,3도 커지게 된다
#즉 a의 섬은 더커지고 group에는 거리에 대한 정보만 기입하는것 
#이런식으로하다가 두칸이 인접했는데 번호가 다르다면(a를 통해 확인) 다리를 건설할수있게 되는거고 그러면 그 각 두칸의 
#거리(group)를 더하면 된다 
from collections import deque
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
g = [[0]*n for _ in range(n)] # group이 저장될곳
d = [[0]*n for _ in range(n)] # 거리가 저장될곳
cnt = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]

#그룹 짓기
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and g[i][j] == 0: #섬인데 그룹이 정해지지 않았다면 
            cnt += 1
            g[i][j] = cnt
            q = deque()
            q.append((i,j))
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if a[nx][ny] == 1 and g[nx][ny] == 0:
                            g[nx][ny] = cnt
                            q.append((nx,ny))

#섬 거리 구하기 및 확장  
q = deque()

#섬은 거리가 0 바다는 -1 로 초기화
for i in range(n):
    for j in range(n):
        d[i][j] = -1
        if a[i][j] == 1:
            q.append((i,j))
            d[i][j] = 0

#섬확장 및 거리구하기
while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if d[nx][ny] == -1:
                d[nx][ny] = d[x][y] + 1
                g[nx][ny] = g[x][y]
                q.append((nx,ny))

ans = -1
#이제 인접한 서로다른 두 그룹의 타일 섬 찾기
for i in range(n):
    for j in range(n):
        for k in range(4):
            x, y = i+dx[k], j+dy[k]
            if 0 <= x < n and 0 <= y < n:
                if g[i][j] != g[x][y]:
                    if ans == -1 or ans > d[i][j] + d[x][y]:
                        ans = d[i][j] + d[x][y]

print(ans)