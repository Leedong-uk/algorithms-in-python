n = int(input())
board = [list(input().rstrip()) for _ in range(n)]
row_check = 0
col_check = 0
row_final = 0
col_final = 0

for i in range(n) : 
    row_check = 0
    for j in range(n) : 
        if board[i][j] == "." :
            row_check += 1
        else:
            if row_check >=2 :
                row_final +=1
                row_check = 0
            else : 
                row_check =0
            
    if row_check >=2 :
        row_final +=1

for i in range(n) : 
    col_check = 0
    for j in range(n) : 
        if board[j][i] == "." :
            col_check += 1
        else :
            if col_check >=2 :
                col_final +=1
                col_check = 0
            else :
                col_check=0

    if col_check >=2 :
        col_final +=1
print (row_final,col_final)
