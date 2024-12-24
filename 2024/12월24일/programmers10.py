brown = 8
yellow = 1
temp = []
result = []


for i in range(1,int(yellow**(0.5))+1) :
    if yellow % i == 0 :
        temp.append([i,yellow//i])

        if (i**2) != yellow :
            temp.append([yellow//i,i])

print(temp)

temp = [[w,h] for w,h in temp if w>=h]
print(temp)

for i in temp : 
    if i[0]*2 + (i[1]+2)*2== brown : 
        result.append(i[0]+2)
        result.append(i[1]+2)

print(result)
