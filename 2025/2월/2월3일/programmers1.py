board = [False] * (n+1)
section = [2,3,6]
result = 0

for i in section : 
    board[i] = True

for i in section :
    if board[i] == True : 
        result +=1
        for j in range(m) : 
            board[(i+j)%n]