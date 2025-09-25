from collections import deque
# n -> 5
# m -> 4
def solution(n,m,hole) : 
    answer = 0 
    board = [[[-1]*2 for _ in range(m)] for _ in range(n)]
    q = deque()
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    jx=[0,0,2,-2]
    jy=[2,-2,0,0]
    
    for x,y in hole : 
        board[x-1][y-1][0] = -2
        board[x-1][y-1][1] = -2

    q.append((0,0,1))
    board[0][0][1] = 0 
    
    while q : 
        x,y,z = q.popleft()

        for k in range(4) : 
            nx , ny = x + dx[k] , y+dy[k]
            if 0<= nx < n and 0 <= ny < m : 
                if board[nx][ny][z] == -1 : 
                    board[nx][ny][z] = board[x][y][z]+1
                    q.append((nx,ny,z))
        
        if z == 1 : 
            for k in range(4) : 
                nx , ny = x + jx[k] , y + jy[k]
                if 0<= nx < n and 0 <= ny < m : 
                    if board[nx][ny][0] == -1 : 
                        board[nx][ny][0] = board[x][y][z] +1 
                        q.append((nx,ny,0))
    
    print(board[n-1][m-1])


    
    return answer 

print(solution(4,4,[[2, 3], [3, 3]]))
print(solution(5,4,[[1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]))