f = int (input())
stack = list(map(int,input().split()))
count= 0 
result = 0
for i in stack : 
    if i > 1 : 
        for x in range(2,i+1) : 
            
            if i % x == 0 :
                count += 1

        if count == 1 : 
            result +=1

        count = 0            
    else : 
        continue

print(result)   
