dartResult = "1D2S#10S"
answer = 0
result = []
S=[False]*11
D=[False]*11
T=[False]*11
star=[False]*11
archer=[False]*11
temp = ""
val=0

for i in range(len(dartResult)) : 
    if dartResult[i].isdigit() : 
        temp +=dartResult[i]
    elif dartResult[i] in ['S','D','T'] : 
        if dartResult[i] == 'S' and S[i] == False :
            result.append(int(temp))
            temp = ''
            S[i] = True
        elif dartResult[i] == 'D' and D[i] == False :
            val = (int(temp)) **2
            result.append(val)
            temp = ''
            D[i] = True
        elif dartResult[i] == 'T' and T[i] == False :
            val = (int(temp)) **3
            result.append(val)
            temp = ''
            T[i] = True
    elif dartResult[i] == '*' and star[i] == False : 
        if len(result) ==1 : 
            result[0] = result[0] *2
        else : 
            result[-2:] =[i*2 for i in result[-2:]]
    elif dartResult[i] == '#' and archer[i] == False :
        result[-1] = result[-1] *(-1)

print(result)
print(sum(result))
