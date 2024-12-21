survey =["TR", "RT", "TR"]
choices =[7, 1, 3]
result =''

select ={1:3,2:2,3:1,4:0,5:1,6:2,7:3}
standard = [['R','T'],['C','F'],['J','M'],['A','N']]
score={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}

for i in range(len(choices)):
    if 1<=choices[i] <=3 :
        score[survey[i][0]] += select[choices[i]]
    
    elif 5<= choices[i] <=7 : 
        score[survey[i][1]] += select[choices[i]]

for i in standard : 
    i.sort()
    if score[i[0]] < score[i[1]] : 
        result += i[1]
    elif score[i[0]] > score[i[1]] : 
        result +=i[0]
    else : 
        result +=i[0]

print(result)

