from collections import deque
from itertools import combinations
from copy import deepcopy

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]  # [x][y] 구조 유지

def bfs(board, check, start_x, start_y):
    q = deque()
    check[start_x][start_y] = 2
    q.append((start_x, start_y))

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if check[nx][ny] == 0 and board[nx][ny] == 0:
                    check[nx][ny] = 2
                    q.append((nx, ny))

def start_virus(board, check):
    for x in range(n):
        for y in range(m):
            if board[x][y] == 2:
                bfs(board, check, x, y)

def count_safe_area(board, check):
    cnt = 0
    for x in range(n):
        for y in range(m):
            if board[x][y] == 0 and check[x][y] == 0:
                cnt += 1
    return cnt

def result():
    blanks =[]
    for x in range( n ) : 
        for y in range( m) : 
            if board[x][y] == 0  :
                blanks.append((x,y))
    max_safe = 0

    for walls in combinations(blanks, 3):
        temp_board = deepcopy(board)
        for x, y in walls:
            temp_board[x][y] = 1  

        check = [[0] * m for _ in range(n)] 
        start_virus(temp_board, check)
        safe = count_safe_area(temp_board, check)
        max_safe = max(max_safe, safe)

    return max_safe

print("최대 안전영역:", result())
