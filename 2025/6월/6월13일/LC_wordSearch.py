# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
# n = len(board)
# m = len(board[0])

# check = [[False]*m for _ in range(n)]

# def dfs(x,y,depth,curr) :
#     if depth == len(word) : 
#         if curr == word : 
#             return True
    
#     for k in range(4) : 
#         nx , ny = x+dx[k] , y+dy[k]
#         if 0 <= nx < n and 0<=ny < m and check[nx][ny] == False : 
#             check[nx][ny] = True
#             if dfs(nx,ny,depth+1,curr+board[nx][ny]) : 
#                 return True
#             check[nx][ny] = False
#     return False

# for i in range(n):
#     for j in range(m):
#         if board[i][j] == word[0]: 
#             check[i][j] = True
#             if dfs(i, j, 1, board[i][j]):
#                 print(True)
#                 exit()
#             check[i][j] = False
# print(False)


# print(dfs(0,0,0,""))



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        n, m = len(board), len(board[0])

        def dfs(x, y, depth):
            if depth == len(word):
                return True
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < m and not check[nx][ny] and board[nx][ny] == word[depth]:
                    check[nx][ny] = True
                    if dfs(nx, ny, depth + 1):
                        return True
                    check[nx][ny] = False
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    check = [[False] * m for _ in range(n)]
                    check[i][j] = True
                    if dfs(i, j, 1):
                        return True
        return False
