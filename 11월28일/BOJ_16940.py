#알고리즘을 꺠달았다 
#이 알고리즘의 주된 목적은 모든 정점에 대하여 부모 노드를 조사해 올바르게 들어가 있는지 확인하는거다
#알고리즘은 이렇게 돌아간다
#옳바른 순서라면 순서는 이렇게 되어있을것이다
#어떤 정수 x가 순서에 들어오면 그 다음에 오는것은 x에서 갈수있는 노드들인 x1,x2(일단 2개로해보겠다)이다
#순서가 저장된 order 배열을 보면 x x1 x2 이렇게 되어있다 
#그러면 이떄 x1, x2의 부모 노드가 다 x가 된다면 이 순서는 옳바르게 된것이다 
#그러면 정수x에대해선 끝냈고 그다음 정수 y 에대해서도 똑같이 진행하면된다 
#이렇게 모든 노드에 대하여 다 조사하면 될것 !
#또하나 중요한게 여기서 order가 우리가 검사해야할 대상이다 즉! 이게 그냥 옳은건지 아닌건지만 판단하면 되는거다\
#다시말하면 order의 순서대로 queue에 저장하면 된다 

#구현방법
#1.BFS를 돌려서 모든 노드에 대하여 자신의 부모노드를 가리키는 정답지를 만든다
#2.정수 x에대하여 x1, x2.....를 조사하고 각 자식 노드들이 부모노드를 정확히 가리키는 지 확인한다
#3.이과정을 모든 노드에 대하여 다 조사해본다 


from collections import deque
n = int(input())
a = [[] for _ in range(n)]
for _ in range(n-1) : 
    u , v = map(int,input().split())
    u -=1
    v -=1
    a[u].append(v)
    a[v].append(u)

order = list(map(int,input().split()))
order = [x-1 for x in order]

check = [False]*n
parent = [-1]*n
q = deque()

q.append(0)
check[0]=True
m=1

for i in range(n) : 
    if not q : 
        print(0)    
        exit()
    
    x = q.popleft()

    if x != order[i] : # order의 순서대로 그대로 큐에 들어갈거기 때문에 
                       #혹시라도 답이 여러개여서 오류가 날지는 걱정 안해도된다
        print(0)
        exit()
    
    cnt = 0

    for y in a[x] : 
        if check[y] == False : 
            parent[y] = x #현재x 에대하여 갈수있는 모든점에 있어서 부모 노드들을 다 결정해줌
            cnt +=1  #그리고 현재 정점에 대하여 갈수있는 정점이 몇개인지도 계산을 해줌
                     # 이는 곧 현재 정점에서는 cnt개 까지 조사가 가능하다는 뜻
    
    for j in range(cnt) : 
        if m+j >=n or parent[order[m+j]] != x : 
            #범위를 벗어나지 않은 경우 or  
            #현재 정점 x에 대하여 현재 정점에서 갈수 있는 정점의 수 m+j 
            #order를 조사해야하니깐 현재정점에서 조사가능한 갯수인 m+j까지의 순서인 order[m+j] 
            #의 parent 값이 현재 x 값(즉 부모값이 됨)이 같아야 올바른 오더라고 할수있다 
            print(0)
            exit()
        q.append(order[m+j])
        check[order[m+j]] = True 
        #order의 특성상 한 정점에 대하여 다음에 오는 정점의 규칙이 있다 
    m +=cnt
print(1)