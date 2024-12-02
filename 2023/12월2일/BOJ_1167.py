#트리의 지름은 아무 노드에서 bfs든 dfs든 을 통해 가장 멀리 있는 노드를 구한후 해당 노드에서
#다시 bfs를 돌려서 가장 멀리있는 노드를 구하면 된다 
from collections import deque
n = int(input())
a = [[] for _ in range(n+1)]



for _ in range(n) : 
    c = list(map(int,input().split()))
    for e in range(1,len(c)-2,2) : 
        a[c[0]].append((c[e],c[e+1]))


def bfs(start) : 
    dist = [-1] *(n+1)
    q = deque()

    q.append(start)
    dist[start] = 0
    _max = [0,0] #노드,거리

    while q: 
        x = q.popleft() #x에대해서
        for y ,z in a[x] :  # y : 노드 , z : 거리
            if dist[y] == -1 : 
                dist[y] = dist[x] + z
                q.append(y)

                if _max[1] < dist[y] : 
                    _max = (y,dist[y])
    
    return _max


node , dis = bfs(1)
print(dis)
node , dis = bfs(node)
print(dis)
print(dis)