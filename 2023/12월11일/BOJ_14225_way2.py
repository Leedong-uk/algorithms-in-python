n = int(input())
a = list(map(int,input().split()))
check = [False]*(n*100000+10)


def go (index,sum) : 
    if index == n : 
        check[sum] = True
        return
    
    go(index+1,sum) #index번쨰 숫자를 포함 하지않는경우
    go(index+1,sum+a[index]) #index번쨰 숫자를 포함 하는경우


go(0,0)

i = 0

while True : 
    if check[i] == False : 
        break
    i +=1

print(i)