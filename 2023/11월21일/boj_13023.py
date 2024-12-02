#두번쨰 방법
#a->b
#b->c
#c->d
#에서 길이가 4인 단순경로를 찾고
#마지막에 d->e를 찾는다 

#인접리스트를 이용하자 

import sys
n,m = map(int,input().split())
A,B,C,D,E = 0
g = [[] for _ in range(n)]

for _ in range(m) : 
    u , v = map(int,input().split()) 
    g[u].append(v)
    g[v].append(u)


    
#BFS #DFS 공부하고 다시찾아오겠습니다

