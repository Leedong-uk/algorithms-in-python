ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
result = 0 
temp = []

for i in ingredient : 
    temp.append(i)
    if len(temp) >=4 and temp[-1] == 1 : 
        if temp[-1:-5:-1] == [1,3,2,1] : 
            result +=1
            del temp[-1:-5:-1]
    
print(result)
