n = int(input())
num = list(map(int,input().split()))
check = [False]*(n*100000+10)
tmp = []

def go (index,sum) : 
    if index == n : 
        check[sum] = True
        return
    
    go(index+1,sum+num[index])
    go(index+1,sum)

go(0,0)
i =1

while True : 
    if check[i] == False : 
        break
    i +=1

print(i)

    
        
