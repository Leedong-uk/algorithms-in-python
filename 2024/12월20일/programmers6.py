board= [["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]]
h=1
w=1
n = len(board)
dh=[0,1,-1,0]
dw=[1,0,0,-1]
count = 0


for i in range(4) : 
    h_check , w_check = h+dh[i] , w+dw[i]
    if 0 <=h_check <n and 0<= w_check <n : 
        if board[h][w] == board[h_check][w_check] : 
            count +=1

print(count)
