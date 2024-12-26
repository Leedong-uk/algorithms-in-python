# matrix = i x j
arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
arr1_i = len(arr1)
arr1_j = len(arr1[0])

arr2_j = len(arr2[0])

result = [[0]*arr2_j for _ in range(arr1_i)]

for i in range(len(result)) :
    for j in range(len(result[0])) : 
        temp = 0
        for k in range (arr1_j) : 
            temp += arr1[i][k] * arr2[k][j]
        
        result[i][j] = temp
print(result)