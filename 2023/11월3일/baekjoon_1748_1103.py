x = int(input())

y = len(str(x))
tmp= 0

ans = 0

for i in range(1,y) : 
    tmp +=9*10**(i-1)*i


ans = tmp + (x-10**(y-1)+1)*y
   
    
print(ans)