#그러면 모든 정점을 한번씩 조사할떄 집이 있으면 그 집에 현재 그룹번호를 부여 하는식으로 가다가
#더이상 갈곳이 없으면  다른 시작점으로 가서 다른 그룹번호를 부여하면서 똑같이 하면된다  

from collections import deque, Counter
from functools import reduce
#dx dy
dx = [0,0,1,-1]
dy = [1,-1,0,0]

#bfs 세팅
def bfs(g,h,cnt) :
    q = deque()
    q.append((g,h))
    group[g][h] = cnt 

    while q :
        x , y = q.popleft()
        for k in range(4) : 
            nx,ny = x + dx[k] , y + dy[k]
            if (0 <= nx < n) and (0 <= ny < n) : 
                if a[nx][ny] == 1 and group[nx][ny] == 0 : 
                    q.append((nx,ny))
                    group[nx][ny] = cnt

n = int(input())
a =  [list(map(int,input())) for _ in range(n)]
group = [[0]*n for _ in range(n)]
cnt = 0



#bfs 실행
for i in range(n) : 
    for j in range(n) : 
        if a[i][j] == 1 and group[i][j] == 0 :
            cnt +=1
            bfs(i,j,cnt)

ans = reduce(lambda x, y : x+y, group)
ans = [x for x in ans if x>0]
ans = sorted(list(Counter(ans).values()))

print(cnt)
print("\n".join(map(str,ans)))