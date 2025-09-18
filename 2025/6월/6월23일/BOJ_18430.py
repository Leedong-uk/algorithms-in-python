n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
max_score = 0

shape = [
    [(0,0), (-1,0), (0,1)],
    [(0,0), (0,-1), (-1,0)],
    [(0,0), (0,-1), (1,0)],
    [(0,0), (1,0), (0,1)],
]

def dfs(x, y, score):
    global max_score
    if y == m:
        x += 1
        y = 0
    if x == n:
        max_score = max(max_score, score)
        return

    if not visited[x][y]:
        for s in shape:
            positions = [(x+dx, y+dy) for dx, dy in s]
            if all(0 <= px < n and 0 <= py < m and not visited[px][py] for px, py in positions):
                # 방문 표시
                for px, py in positions:
                    visited[px][py] = True

                # 점수 계산 (중심 2배)
                center_x, center_y = positions[0]
                temp_score = board[center_x][center_y]*2 + sum(board[px][py] for px, py in positions[1:])

                dfs(x, y+1, score + temp_score)

                # 방문 해제
                for px, py in positions:
                    visited[px][py] = False
    dfs(x, y+1, score)

dfs(0,0,0)
print(max_score)
