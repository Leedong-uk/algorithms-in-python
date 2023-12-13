#각각의 벽에 대해서 벽을 부시고 그 부신벽을 기준으로 이동가능한 칸의 갯수를 출력
#당연히 기존에 0 이였던 이동 가능한곳은 0을 출력
#시간초과 떴음
"""from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n, m = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(n)]
group = [[0]*m for _ in range(n)]


def bfs(x,y) : 
    check = [[False]*m for _ in range(n)]
    q = deque()
    q.append((x,y))
    check[x][y] == True 
    cnt = 1
    while q : 
        x,y = q.popleft()
        for k in range(4) : 
            nx,ny = x+dx[k] , y +dy[k]
            if 0<= nx < n and 0 <= ny < m :
                if check[nx][ny] == False and a[nx][ny] == 0 :
                    check[nx][ny] = True
                    q.append((nx,ny))
                    cnt +=1
    
    return cnt


for i in range(n) : 
    for j in range(m) : 
        if a[i][j] == 1 and group[i][j] == 0 : 
            cnt = bfs(i,j)
            group[i][j] = cnt 

for i in range(len(group)) : 
    for j in group[i] : 
        print(j,end='')
    print()"""

#인접해있는 그룹을 니어에 다 넣어줌 
#거기를 set 으로 바꿔서 중복 제거 
#그룹번호 만들어줌 , 그룹의 크기도 

#1.그룹짓기(맨처음 벽을 부시지않고 갈수있는 곳들)(이떄 그룹의 크기도 구하기)
#2.그룹짓고 한 타일에 대해서 위아래에 어떤 그룹이 있는지 확인
#3.그룹을 중복되지않고 구하기
#4.1+각 그룹의 크기 구해서 표현하기 

from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n, m = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(n)]
group = [[-1]*m for _ in range(n)]
check = [[False]*m for _ in range(n)]
group_size = []


def bfs(sx, sy):
    g = len(group_size)
    q = deque()
    q.append((sx,sy))
    group[sx][sy] = g
    check[sx][sy] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if check[nx][ny] == False and a[nx][ny] == 0:
                    check[nx][ny] = True
                    group[nx][ny] = g
                    q.append((nx,ny))
                    cnt += 1
    
    group_size.append(cnt)

#그룹짓기
for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and check[i][j] == False:
            bfs(i, j)

#각 칸에 대해서 인접한 그룹 조사하기
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            print(0, end='')
        else:
            near = set()
            for k in range(4):
                nx,ny = i+dx[k],j+dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] == 0:
                        near.add(group[nx][ny]) #그룹번호가져와서
            ans = 1
            for g in near:
                ans += group_size[g] #그룹 크기 다 더함 
            print(ans%10, end='')
    print()

    


