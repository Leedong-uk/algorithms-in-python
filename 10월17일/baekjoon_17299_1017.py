from collections import Counter

n = int(input())

A = list(map(int,input().split()))
Count_num = Counter(A)
result = [None]*n
Stack =[]


for i in range(len(A)) : 
    while Stack and Count_num[A[Stack[-1]]] < Count_num[A[i]] : 
        result[Stack.pop()] = A[i]


    Stack.append(i) 


while Stack : 
    result[Stack.pop()] = -1


print(" ".join(list(map(str,result))))
