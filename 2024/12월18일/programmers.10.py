n=4
m=1
section = [1,2,3,4] 
board = [True] *8
answer =0
for i in section : 
    board[i] = False

for i in section : 
    if board[i] == False : 
        answer +=1
        for j in range(m) : 
            board[(i+j)%n] = True
        

print(answer)

