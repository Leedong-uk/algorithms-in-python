from itertools import permutations
numbers = "17"
max_num = int("".join(sorted(numbers, reverse=True)))
cnt = 0
checked = set()
board = [True] * (max_num+1)
board[0] = False
board[1] = False
for i in range(2,int((max_num+1)**0.5)+1) : 
    if board[i] == True : 
        for j in range(i*2,(max_num+1),i) :
            board[j] = False


for i in range(1,len(numbers)+1) : 
    for j in set(permutations(numbers,i)) : 
        x = int("".join(j))
        if x not in checked and board[x] : 
            cnt +=1
            checked.add(x)

print(cnt)

