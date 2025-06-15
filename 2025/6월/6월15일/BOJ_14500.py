n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        # ㅡ 모양 
        if j + 3 < m:
            x = board[i][j] + board[i][j+1] + board[i][j+2] + board[i][j+3]
            ans = max(ans, x)

        # ㅣ 모양 
        if i + 3 < n:
            x = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j]
            ans = max(ans, x)

        # ㅁ 모양 
        if i + 1 < n and j + 1 < m:
            x = board[i][j] + board[i][j+1] + board[i+1][j] + board[i+1][j+1]
            ans = max(ans, x)

        # L자 모양 (8가지 회전)
        if i + 2 < n and j + 1 < m:
            ans = max(ans,
                      board[i][j] + board[i+1][j] + board[i+2][j] + board[i+2][j+1],
                      board[i][j+1] + board[i+1][j+1] + board[i+2][j+1] + board[i+2][j],
                      board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+2][j+1],
                      board[i][j] + board[i+1][j] + board[i+2][j] + board[i][j+1],
                      board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2],
                      board[i][j+2] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2])

        # ㄴ자 모양 (8가지 회전)
        if i + 1 < n and j + 2 < m:
            ans = max(ans,
                      board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j],
                      board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+2],
                      board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2],
                      board[i+1][j] + board[i+1][j+1] + board[i+1][j+2] + board[i][j+2])

        # 번개 (Z자) 모양
        if i + 2 < n and j + 1 < m:
            ans = max(ans,
                      board[i][j] + board[i+1][j+1] + board[i+1][j] + board[i+2][j+1],
                      board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+2][j])

        if i + 1 < n and j + 2 < m:
            ans = max(ans,
                      board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i][j+2],
                      board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+1][j+2])

        # ㅗ, ㅜ, ㅏ, ㅓ 모양 
        if i + 1 < n and j + 2 < m:
            x = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+1]
            ans = max(ans, x)
        if i + 2 < n and j + 1 < m:
            x = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+1][j+1]
            ans = max(ans, x)
        if i + 1 < n and j + 2 < m:
            x = board[i+1][j] + board[i+1][j+1] + board[i+1][j+2] + board[i][j+1]
            ans = max(ans, x)
        if i + 2 < n and j + 1 < m:
            x = board[i][j+1] + board[i+1][j+1] + board[i+2][j+1] + board[i+1][j]
            ans = max(ans, x)

print(ans)
