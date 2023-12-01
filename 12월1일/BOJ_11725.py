#트리는 bfs는 dfs든 다 최단거리를 구할수있다 
#트리의 탐색은 dfs든 bfs는 똑같이 가능하다 트리는 어차피 노드사이의 간선이 1개뿐인 그래프이기 때문이다 
from collections import deque
n = int(input())
a = [[] for _ in range(n+1)]
parent = [-1]*(n+1) #방문안했으면 -1 방문했으면 : 부모노드의 수
q = deque()
for _ in range(n-1) : 
    u , v = map(int,input().split())
    a[u].append(v)
    a[v].append(u)

parent[1] = 0
q.append(1)

while q : 
    x = q.popleft() 
    for y in a[x] :
        if parent[y] == -1 : 
            parent[y] = x
            q.append(y)


for i in range(2,n+1):
    print(parent[i])


