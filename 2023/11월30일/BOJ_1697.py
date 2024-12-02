# 최대치도 이용할줄 알아야함
from collections import deque
MAX = 200000
start , end = map(int,input().split())
check = [False] *(MAX+1)
dist = [-1]*(MAX+1)
q = deque()

check[start] = True
dist[start] = 0
q.append(start)

while q : 
    now = q.popleft()
    for next in [now+1,now-1,now*2] : 
        if 0<=next <MAX and check[next] == False :
            check[next]= True
            dist[next] = dist[now]+1
            q.append(next)
 


print(dist[end])
