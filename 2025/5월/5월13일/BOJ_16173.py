from collections import deque

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
check = [[False]*n for _ in range(n)]


q = deque()
check[0][0] = True
q.append((0,0))

while q : 
    x ,y = q.popleft()
    value = board[x][y]
    
    if value == -1:
        print("HaruHaru")
        exit(0)
    
    case1_x , case1_y = x+value , y
    case2_x , case2_y = x , y+value
    
    if 0<= case1_x < n and 0<= case1_y < n and check[case1_x][case1_y] == False : 
        check[case1_x][case1_y] = True
        q.append((case1_x,case1_y))
    
    if 0<= case2_x < n and 0<= case2_y < n and check[case2_x][case2_y] == False : 
        check[case2_x][case2_y] = True
        q.append((case2_x,case2_y))

print("Hing")

    