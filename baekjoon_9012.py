n = int(input())
n1 = 0
while True : 
    if n1 == n :
        break

    n3 = list(input())
    
    result = 0
    for i in n3 : 
        stop =1 
        if i =="(":
            result = result +1
        elif i :
            result = result -1
        
        if result<0 : 
            print("NO")
            stop = 0
            break
    if result==0 and stop==1 :
        print("YES")  
    elif result != 0 and stop ==1: 
        print("NO")

    n1 = n1+1