from collections import deque
import sys
MAX = 10001
sys.setrecursionlimit(MAX)

def go(n, m):
    if n == m:
        return
    go(n, via[m])
    print(how[m], end='')

n  = int(sys.stdin.readline())
for _ in range(n) :
    start , end = map(int,input().split())
    q = deque()
    dist = [-1] * MAX # dist[도착한 값] = 방법수  :  -1 :도착 x , 정수 : 도착 최소값
    via = [-1] * MAX  # via[도착한 값] = '어떤수로부터 왔나 ?'
    how = [''] * MAX  # how[도착한 값] = '어떤 방법으로?'


    q.append(start)
    dist[start] = 0
    via[start] = 0
    how[start] = 0

    while q : 
        x = q.popleft()
        str_x = str(x)

    #D 실행
        D_x = x*2
        if D_x >9999 : 
            D_x = D_x % 10000
            if dist[D_x] == -1 : 
                dist[D_x] = dist[x]+1
                via[D_x] = x
                how[D_x] = 'D'
                q.append(D_x)
    
        elif dist[D_x] == -1 : 
            dist[D_x] = dist[x]+1
            via[D_x] = x
            how[D_x] = 'D'
            q.append(D_x)
    
        #S실행
        S_x = x-1
        if S_x <0 :
            if dist[S_x] == -1 : 
                dist[9999] = dist[x]+1
                via[9999] = x
                how[9999] = 'S'
                q.append(9999)
        else : 
            if dist[S_x] == -1 :
                dist[S_x] = dist[x]+1
                via[S_x] = x
                how[S_x] = 'S'
                q.append(S_x)
    
        #L실행
        L_x = (x%1000)*10 + x//1000
        if dist[L_x] == -1 :
            dist[L_x] = dist[x]+1
            via[L_x] = x
            how[L_x] = 'L'
            q.append(L_x)
    
        #R실행
        R_x = (x//10) + (x%10)*1000
        if dist[R_x] == -1 : 
            dist[R_x] = dist[x]+1
            via[R_x] = x
            how[R_x] = 'R'
            q.append(R_x)


    go(start,end)
    print()

    
    



