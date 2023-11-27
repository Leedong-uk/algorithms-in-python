"""


    
                     # 특이한점은 보통 bfs는 이미 방문한점을 다시 가기싫어서 false인 상황만 돌린다
                     #근데 여기에선 다시 방문할수있게한다 
                     # 그니깐 좋건에 만족하는 범위 안에 있는 nx ny 중 에서 판단하는거
                     # 근데 중복 검토를 계속 해야하는데 괜찮은가 
                    return True


for i in range(n) : 
    for j in range(m) : 
        if check[i][j] : 
            continue
        dist = [[0]*m for _ in range(n)] #방문한 갯수를 저장할 것
        ok = dfs(i, j, 1)
        if ok:
            print('Yes')
            exit()
print('NO')"""
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n,m = map(int,input().split())
a = [input() for _ in range(n)]
dist = [[0]*m for _ in range(n)]
check = [[False]*m for _ in range(n)]

def go(x, y, cnt, color):
    if check[x][y]: # 이미 방문한 점인데 
        if cnt-dist[x][y] >= 4:
            # 현재 상황 : 이미 방문한 "점 x" 에 다시 방문하였다
            #  dis[x][y] : 처음 x에 방문했을떄 걸린 방문횟수 ,  cnt : 다시 x에 방문했을떄 걸린 방문횟수
            # 이 둘의 차가 4이 상이면 크기가 4이상인 cycle이 완성된다
            return True
        else:
            return False
        
    check[x][y] = True
    dist[x][y] = cnt

    for k in range(4):
        nx,ny = x+dx[k],y+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == color:
                if go(nx,ny,cnt+1,color):
                    # 특이한점은 보통 bfs는 이미 방문한점을 다시 가기싫어서 false인 상황만 돌린다
                     #근데 여기에선 다시 방문할수있게한다 
                     # 그니깐 좋건에 만족하는 범위 안에 있는 nx ny 중 에서 판단하는거
                     # 근데 중복 검토를 계속 해야하는데 괜찮은가
                    return True
    return False


for i in range(n):
    for j in range(m):
        if check[i][j]:
            continue
        dist = [[0]*m for _ in range(n)]
        ok = go(i, j, 1, a[i][j])
        if ok:
            print('Yes')
            exit()
print('No')







#근데 사이클이 처음과 끝이 같아야하잖아 이건 어떻게 처리할건데 ?



