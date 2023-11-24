#최초 : case 수
#첫번쨰칸 : 체스판 한변의 길이 l
# 4 <= l <= 300 , 체스판크기 l x l , 체스판의 각 칸은 0 ~ l-1
#두번쨰 칸 : 나이트가 현재 있는칸 ->here_x , here_y
#세번쨰 칸 : 나이트가 이동하려고 하는 칸 (목표)->goal_x ,goal_y

#★★★★★★★★꺠달았다 최초에 배열을 초기화할떄 수의 범위 밖에 있는 값으로 해야함 ★★★★★★★★★★

from collections import deque

dx=[-2,-1,1,2,2,1,-1,-2]
dy=[1,2,2,1,-1,-2,-2,-1]


def bfs(x,y):
    while q : 
        x,y = q.popleft()
        cnt = a[x][y]
        for k in range (8) : 
            nx , ny = x+dx[k] , y+dy[k]
            if (0 <= nx < l) and (0 <= ny < l) : 
                if a[nx][ny] == -1 :
                    q.append((nx,ny))
                    a[nx][ny] = cnt+1



n = int(input())
for _ in range(n) : 
    q = deque()
    l = int(input())

    a = [[-1]*l for _ in range(l)]

    here_x , here_y = map(int,input().split())
    goal_x , goal_y = map(int,input().split())

    """
    if (here_x,here_y) == (goal_x,goal_y) : 
        print(0)
        break
        """
    q.append((here_x,here_y))
    a[here_x][here_y] = 0

    bfs(here_x,here_y)

    print(a[(goal_x)][goal_y])


