from collections import deque 

def numIslands(grid): 
    answer = 0
    n = len(grid)
    m = len(grid[0])
    visited = [[False] * m for _ in range(n)]

    for i in range(n): 
        for j in range(m): 
            if grid[i][j] == "1" and not visited[i][j]: 
                dfs(grid, i, j, visited, n, m)
                answer += 1
    return answer

def dfs(grid, x, y, visited, n, m): 
    q = deque()
    q.append((x, y))
    visited[x][y] = True 
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q: 
        x, y = q.popleft()
        for k in range(4): 
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == "1" and not visited[nx][ny]: 
                    visited[nx][ny] = True 
                    q.append((nx, ny))


print(numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))  # 1

print(numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))  # 3
