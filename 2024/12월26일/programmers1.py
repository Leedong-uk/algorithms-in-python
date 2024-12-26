s="}}}"
result = 0
s = list(s)


for i in range(len(s)) : 
    s_list = [s[(j + i) % len(s)] for j in range(len(s))] 
    print(i,'번쨰','현재s_list :',s_list)
    temp = []
    temp.append(s_list.pop())

    while s_list : 
        x = s_list.pop()
        if len(temp) >=1 and x == "{" and temp[-1] == '}' :
            temp.pop()
        elif len(temp) >=1 and x == "(" and temp[-1] == ')' :
            temp.pop()
        elif len(temp) >=1 and x == "[" and temp[-1] == ']' :
            temp.pop()
        else : 
            temp.append(x)
    
    print('tmep 결과 :',temp)
    if not temp:
        result +=1

print(result)
        


        

    
    