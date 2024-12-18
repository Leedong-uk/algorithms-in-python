n = int(input())
temp = []
number = []
index = 0 
for i in range(n) :
    temp = [] 
    x = input()
    for j in x : 
        temp.append(j) 
    
    for j in range (len(x)) : 
        if temp[j].isdigit() : 
            if j>0 and temp[j-1].isdigit() : 
                number[-1] = number[-1]+temp[j]
            else : 
                number.append(temp[j])
               

result = list(map(int,number))
result.sort()
for i in result : 
    print(i)



