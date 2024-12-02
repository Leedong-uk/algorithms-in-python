from collections import deque
import sys
MAX = 200000
sys.setrecursionlimit(MAX)
start , end = map(int,input().split())
check = [False] *(MAX+1)
dist = [-1]*(MAX+1)
q = deque()

a = [[] for _ in range(MAX+1)]
tmp = []

check[start] = True
dist[start] = 0
q.append(start)


while q : 
    now = q.popleft()
    for next in [now-1,now+1,now*2] : 
        if 0<=next <MAX and check[next] == False :
            check[next]= True
            dist[next] = dist[now]+1
            a[now].append(next)
            a[next].append(now)
            q.append(next)





tmp.append(end)
def ans(end) : 
    cnt = dist[end]    
    for i in a[end] : 
        if dist[i] < cnt : 
            tmp.append(i)
            ans(i)

ans(end)
tmp.reverse()
print(dist[end])
print(" ".join(map(str,tmp)))


