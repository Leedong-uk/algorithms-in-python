import sys
num = 1000001
stack = [True]*num



for i in range(2, int((num-1)**0.5)+1) : 
    if stack [i] : 
        for j in range(i*2,num,i) : 
            stack[j] = False

x =  int(sys.stdin.readline().rstrip())

for _ in range(x) : 
    n = int(sys.stdin.readline().rstrip())
    count = 0 

    for i in range(2,int(n/2)+1) :
        if stack [i] and stack[n-i] : 
           
            count+=1

    print(count)        
    
