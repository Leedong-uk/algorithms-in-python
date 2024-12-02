#일단 이 문제에선 인접행렬 인접리스트를 만들 필요가 없음 
#위에 두개를 만드는 목적은 하나의 정점에 연결된 간선을 효율적으로 찾아보기 위해서인데 
# 얘 는 그냥 그런거 할필요없이 위 아래 를 검사하면 되는거임 (그래프처럼 막 뒤섞여 있는게아니라)
#그 대신 검사를 할떄 bfs dfs 를 쓰는거임 왜냐 이 둘의 목적은 모든 정점을 한번씩 다 가는거기 때문에
#그럼 한번씩 다 갈떄 조건을 몇개 걸어주면 되는거
#근데 보면 연결 요소 파악하는 문제와 매우 유사한다는걸 알수있음
#그러면 모든 정점을 한번씩 조사할떄 집이 있으면 그 집에 현재 그룹번호를 부여 하는식으로 가다가
# 더이상 갈곳이 없으면  다른 시작점으로 가서 다른 그룹번호를 부여하면서 똑같이 하면된다  

from collections import deque, Counter
from functools import reduce

n = int(input())
a = [list(map(int,(input()))) for _ in range(n)]
group = [[0]*n for _ in range(n)]
cnt = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y,cnt): #x행 y열 그리고 방문체크 cnt : 0 or 그룹번호
    group[x][y] = cnt #최초는 시작점 그룹을 정해주고 
    for k in range(4) : 
        nx,ny = x+dx[k] ,y+dy[k] #시작점에 대하여 위아래 양옆 다 조사해봄
        if 0 <= nx <n and 0 <= ny < n : #범위내에 있으면
            if a[nx][ny] == 1 and group[nx][ny] == 0 : #어떻게 조사하냐? 시작점 기준으로 집이 있고  ,방문한적이 없으면 같은 그룹이란소리
                dfs(nx,ny,cnt)# 그럼 그쪽 그룹으로 가서 현재cnt값을 넣어줌

for i in range(n): #모든 노드에 대해서 그룹을 짓기 시작함 
    for j in range(n): 
        if a[i][j] ==1 and group[i][j] == 0 :
            cnt+=1
            dfs(i,j,cnt)




print(cnt)
ans = reduce(lambda x,y : x+y, group) # 2차원 행렬을 1차원행렬 1줄로 만듬
ans = [x for x in ans if x > 0] # 0 제거
ans = sorted(list(Counter(ans).values()))
# ans를 counter에 넣어서 사전형식으로 
# 1: 1빈도수 2 : 2 빈도수 ..... 이런식으로 만듦
#이떄 빈도수만 가져오는 즉 key값이 아닌 value 값만 가져오는 .values()를 써서 dic_value형태로 반환이되고
#그걸 list형태로 다시만든다음 정렬을해서 print함
 
print(ans)




