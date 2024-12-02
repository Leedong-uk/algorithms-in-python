# 어떻게 이게 bfs dfs를 할수있을까 ? 
#일단 check[x][y] = True 면 이미 돌이 x개 y개 인걸 만들수 있고 방문한적이 있다는 뜻이다
#따라서 x//3 y//3 이 true 라면 ? 돌을 3분할 가능하단 뜻이다 
from collections import deque
import sys
sys.setrecursionlimit(1500*1500)
check = [[False]*1501 for _ in range(1501)]
x,y,z = map(int,input().split())
s = x+y+z
def go (x,y) : 
    q = deque()
    q.append((x,y))
    check[x][y] = True

    while q : 
        x,y = q.popleft()
        a = [x,y,s-x-y]

        for i in range(3) : 
            for j in range(3) : 
                if a[i] < a[j] : 
                    b = [x,y,s-x-y]
                    b[i] +=a[i]
                    b[j] -=a[i]
                    if check[b[0]][b[1]] == False : 
                        check[b[0]][b[1]] = True
                        q.append((b[0],b[1]))







if s % 3 != 0:
    print(0)
else:
    go(x,y)
    if check[s//3][s//3]:
        print(1)
    else:
        print(0)
