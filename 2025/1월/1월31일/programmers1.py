m = 4
n = 5
board = [list("CCBDE"), list("AAADE"), list("AAABF"), list("CCBBF")]
answer = 0  # 삭제된 블록 개수 저장


def find(board):
    check = [[False] * n for _ in range(m)]
    for i in range(m - 1):
        for j in range(n - 1):
            block = board[i][j]
            if block != '' and block == board[i + 1][j + 1] and block == board[i + 1][j] and block == board[i][j + 1]:
                check[i][j] = True
                check[i + 1][j] = True
                check[i][j + 1] = True
                check[i + 1][j + 1] = True
    return check



def remove_blank(board, check):
    global answer
    for i in range(m):
        for j in range(n):
            if check[i][j]:  
                board[i][j] = '' 
                answer += 1 
    return board



def rearrange(board):
    for j in range(n): 
        cnt = 0 
        for i in range(m - 1, -1, -1):  
            if board[i][j] == '':
                cnt += 1  
            elif cnt > 0:
                board[i + cnt][j] = board[i][j]  
                board[i][j] = ''  
    return board



while True:
    check = find(board)  
    if not any(any(row) for row in check):  
        break

    board = remove_blank(board, check) 
    board = rearrange(board)  


print(answer)
