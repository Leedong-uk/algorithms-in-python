from collections import deque
# 0 : 가로 방향 / 1: 세로 방향
dx = [0,0,1,-1]
dy = [1,-1,0,0]
board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
n = len(board)
check = [[[0] * 2 for _ in range(n)] for _ in range(n)]

q = deque()
q.append(((0,0),0))
check[0][0][0] = 1 

def is_valid(x,y) : 
    return 0 <= x < n and 0 <= y < n and board[x][y] == 0

while q: 
    x,y,z = q.popleft()
    value = check[x][y][z]
    
    if (x == n-1 and y == n-2 and z == 0) or (x==n-2 and y==n-1 and z == 1) : 
        print(value -1)
        break
    
    for k in range(4) : 
        left_nx,left_ny = x+dx[k] , y+dy[k] 
        
        # 오른쪽 바퀴 좌표 구하기
        if z == 0 : 
            right_nx , right_ny  = left_nx,left_ny+1
        else : 
            right_nx,right_ny = left_nx+1,left_ny
        
        if is_valid(left_nx,left_ny) and is_valid(right_nx,right_ny) : 
            if check[left_nx][left_ny][z] == 0 :
                check[left_nx][left_ny][z] = value+1
                q.append((left_nx,left_ny,z))
        
        #가로->세로 
        if z == 0 : 
            for d in [-1,1] : 
                left_nx = x+d
                if 0<= left_nx < n :
                    if is_valid(left_nx,y) :
                        if check[x][y][1] == 0 : 
                            check[x][y][1] = value +1
                            q.append(((x,y),1))
                    
                    if is_valid(left_nx,y+1) : 
                        if check[x][left_ny][1] == 0 :
                            check[x][left_ny][1] = value +1
                            q.append(((x,left_ny),1))
        #세로 ->가로
        if z == 1 : 
            for d in [-1,1] : 
                left_ny = y+d
                if 0<= left_ny < n : 
                    if is_valid(x,left_ny) : 
                        if check[x][y][0] == 0 : 
                            check[x][y][0] = value +1
                            q.append(((x,y),0))
                    if is_valid(x+1,left_ny) : 
                        if check[x+1][y][0] == 0 :
                            check[x+1][y][0] = value+1
                            q.append(((x+1,y),0))
                    
            
        