x = int(input())

n = x // 5 

while n >=0 : 
    remainder = x - (5*n)
    
    if (remainder %3 == 0 ) :
        print(n + (remainder//3))
        break
    
    n -=1

else : print(-1)