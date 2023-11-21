import sys
n,m = map(int,input().split())
edges = [] #간선리스트 
           #a와 b 그리고 c와 d 가연결된 모든것을 찾을떄 모든 간선이 있는 간선list에서 간선을 순회하면서 찾는다
a = [[False]*n for _ in range(n)] #인접행렬
                                  #인접행렬의 유일한장점 2개의 정점을 알떄 그 정점사이에 간선의 유무를 파악할떄 적은시간이 걸림
                                  
g = [[] for _ in range(n)] #인접리스트
                           #그래프 알고리즘에서 많이 쓰이는 한정점과 연결되어있는 모든 간선을 파악하기 위해서 쓰임

for _ in range(m) : 
    u,v = map(int,input().split()) 

    #간선리스트를 만듬 이때 친구관계는 양방향임을 잊지말자
    edges.append((u,v)) 
    edges.append((v,u)) 

    #인접행렬에도 넣어줌
    a[u][v] = True
    a[v][u] = True

    #마지막 인접 리스트도 넣어줌
    g[u].append(v)
    g[v].append(u)

m = m*2 #이걸왜해주냐 친구관계->양방향->간선이 2개씩 생김 !! 모든간선을 순회하기위해서 최대값이 필요함

for i in range(m) : 
    for j in range(m) : 
        A ,B = edges[i]
        C ,D = edges[j] #간선리스트에서 A,B,C,D 이친구들 다 찾음

        if A == B or A ==C or A == D or B==C or B==D or C ==D : #ABCD는 모두 달라야 함으로 여기서 한번 filtering 해줌
            continue
        #------------------------여기까지 일단 a,b,c,d완료했음 즉 2번 과정까지 완료

        #3번과정인 b와c사이에 간선이 있는지 확인 
        if  not(a[B][C]) or not(a[C][B]) : 
            continue

        #마지막 4번과정 작성 
        for E in g[D] : 
            if A == E or B== E or C==E or D==E : #abcde는 전부 다 달라야 함으로 
                continue
            print(1)
            sys.exit(0)
print(0)