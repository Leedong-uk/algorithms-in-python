size= 1000001
n=437674
k=3
#에스테.... 의 체
board = [True] *size  
board[0] = False
board[1] = False

for i in range(2,int(size**0.5)+1) : 
    for j in range(i*2,size,i) : 
        board[j] = False

#진법변환
temp = ""
while n : 
    temp += str(n%k)
    n = n // k 

temp = temp[::-1]

#0기준으로 나눈후 소수 판별
li = []
li = [x for x in temp.split('0') if x]
result = 0 

for i in li : 
    if i.isdigit() and int(i) < size and board[int(i)]:
        result +=1

print(result)





