n = int(input())
result=[]
i = 666
flag = False
while True : 
    k = str(i)
    if '666' in k : 
        result.append(int(k))
        
    if (len(result)) == n :
        break

    i +=1

print(result[n-1])
    

