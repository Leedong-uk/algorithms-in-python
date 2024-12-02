from collections import deque
n , m  , start =  map(int,input().split()) # n : 노드의수 , m : 간선의수 , v : 시작정점
a = [[] for _ in range(n+1)] #인접리스트 
check = [False] *(n+1)
q = deque()


#인접리스트 만들기
for _ in range( m ) : 
    u,v = map(int,input().split())
    a[u].append(v)
    a[v].append(u)

for i in range(1,n+1) : 
    a[i].sort()


def dfs(x) : 
    check[x] = True
    print(x , end= " ")
    for i in a[x] :
        if check[i] == False :
            dfs(i)


def bfs(start) : 
    check = [False] *(n+1)
    q.append(start) # 1.시작점 큐에 기입
    check[start] = [True] #2.시작점 노드  true

    while q : 
        x = q.popleft()
        print(x , end=" ")     
        for i in a[x] : 
            if check[i] == False:
                q.append(i)
                check[i] = True




dfs(start)
print()
bfs(start)
print()