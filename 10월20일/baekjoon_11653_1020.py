n = int(input())

if n ==1 : 
    exit()
else:
    num = 10000001
    stack = [True]*num


#소수찾기
    for i in range(2,int((num-1)**0.5)+1) : 
        if stack[i] : 
            for j in range(i*2,num,i) : 
                stack[j] = False



    for i in range(2,int((num-1)**0.5)+1) : 
        if stack[i] and n%i == 0 :
            while n%i == 0 :
                print(i)
                n = n//i
            

