
import sys 
n = int(input())
answer = [None] *n
A = list(map(int,input().split()))
index_Stack = []


for i in range(n) : 
    while index_Stack and A[index_Stack[-1]] < A[i] : 
        answer[index_Stack.pop()] = A[i]
        

    index_Stack.append(i)
    
   

while index_Stack : 
    answer[index_Stack.pop()] = -1


print(" ".join(list(map(str,answer))))
                                                                                                    