s = "banana"
check = [0,0]
answer=0
stand = s[0]
for i in range(0,len(s)) : 
    
    if s[i] == stand :
        check[0] +=1
    else : 
        check[1] +=1
    
    if i < len(s)-1 and check[0] == check[1] :
        answer +=1
        stand = s[i+1]
        check=[0,0]

print(answer+1)


