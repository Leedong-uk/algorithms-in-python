from collections import deque
def solution(maps) : 
    answer = 0
    n = len(maps)
    m = len(maps[0])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    check = [[-1]* m for _ in range(n)]
    q = deque()

    if maps[0][0] == 0 : 
        return -1

    check[0] = 0
    q.append((0,0))

    while q: 
        x,y = q.popleft()
        value = check[x][y]
        for k in range(4) : 
            nx , ny = x+dx[k] , y+dy[k]

            if (0<= nx < n and 0<= ny < m) : 
                if check[nx][ny] == -1 and maps[nx][ny] == 1 : 
                    check[nx][ny] = value +1
                    q.append((nx,ny))
    
    answer = check[n-1][m-1]+1

    return answer



solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])