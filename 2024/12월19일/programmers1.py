n =5
check = [0] *(n+2)
result = []
answer = []
stages = [2, 1, 2, 6, 2, 4, 3, 3]
for i in stages : 
    check[i] +=1

for j in range(1,(n+1)) : 
        result.append([j, check[j]/sum(check[j:])])

print(result)

result.sort(key=lambda x : x[1],reverse = True)
print(result)
for index, val in result : 
    answer.append(index)
print(answer)

