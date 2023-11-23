"""import sys
sys.setrecursionlimit(1000000)
k= int(input())


def dfs (x) : 
    check[x] = True
    if team[x] == False : 
        team[x] = 1

    for i in a[x] : 
        if check[i] == False :
            if team[x] == 1 :
                team[i] = 2
                dfs(i)
            else:
                team[i] =1
                dfs(i)
            

for _ in range(k) : 
    #각 테스트의 대하여 필요한 것들 초기화
    v , e = map(int,input().split())
    check = [False]*(v+1)
    a = [[] for _ in range(v+1)]
    team = [False]*(v+1)


    #인접리스트 세팅
    for _ in range(e) : 
        x , y  = map(int,input().split())
        a[x].append(y)
        a[y].append(x)
    
    dfs(1)

    for i in range(1,v+1) : 
        for j in a[i] : 
            if team[i] == team[j] : 
                print("NO")
                sys.exit(0)
                


    print("YES")"""

#메모리초과 떴음 씹

import sys
sys.setrecursionlimit(1000000)
t = int(sys.stdin.readline())

for _ in range(t) : 
    #각 테스트의 대하여 필요한 것들 초기화
    n , m = map(int,sys.stdin.readline().split())
    a = [[] for _ in range(n)]
    check = [False]*n 

    #인접리스트 세팅
    for _ in range(m) : 
        u , v = map(int,sys.stdin.readline().split())
        a[u-1].append(v-1)
        a[v-1].append(u-1)

    #dfs 세팅
    def dfs (x,c) : #x노드에 c라는 팀 번호를 기입함
        check[x] = c #1번이라고 정하는게아니라 c를 그냥 받아오면 되는구나!!!
        for i in a[x] : 
            if check[i] == False :
                dfs(i,3-c)
    
    ans = True
    for i in range(n) : #어떤 번호부터 이게 시작할지 , 또 중간에 어디 끊어진게 있는지 
        if check[i] == 0 : 
            dfs(i,1)


    for i in range(n):
        for j in a[i]:
            if check[i] == check[j] : 
                ans = False
    
    print('YES' if ans else 'NO')






    