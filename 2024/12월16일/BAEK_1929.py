n , m = map(int,input().split())
board = [True] * (m+1)
board[0] = False
board[1] = False

for i in range(2,int((m+1)**(0.5))+1) : 
    if board[i] == True :
        for j in range(i*2,(m+1),i) : 
            board[j] = False 


for k in range(n,m+1) : 
    if board[k] :
        print(k)