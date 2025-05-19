from collections import deque
R , C = map(int,input().split())
dx = [0,0,1,-1]
dy = [1,-1,0,0]
board = [list(input()) for _ in range(R)]
check_alpha = set()
q = deque()
max_depth = 0
def dfs(x,y,depth) : 
    # 종료 조건 추가
    global max_depth
    max_depth = max(max_depth,depth)
    
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < R and 0 <= ny < C:
            if board[nx][ny] not in check_alpha: 
                check_alpha.add(board[nx][ny])
                dfs(nx,ny,depth+1)
                check_alpha.remove(board[nx][ny])

check_alpha.add(board[0][0])
dfs(0,0,1)
print(max_depth)

