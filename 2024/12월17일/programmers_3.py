arr1 = [9,20,28,18,11]
arr2 = [30,1,21,17,28]
result = []
answer = []

for i in range(len(arr1)) : 
    tmp = format(arr1[i]|arr2[i],'b')
    result.append(tmp)

for word in result :
    temp=''
    for i in range(len(word)) :
        if word[i] == '1' : 
            temp += "#"
        else : 
            temp +=' '
    answer.append(temp)

print(answer)
