n = 4
temp = []
left = 7
right = 14

for i in range(left,right+1) : 
    temp.append(max(i//4,i%4)+1)

print(temp)