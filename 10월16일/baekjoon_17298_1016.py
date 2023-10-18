"""import sys
n = int(sys.stdin.readline().rstrip())
size = n
a = list(map(int,sys.stdin.readline().split()))
tmp = []
result = []

for i in range(0,size) : 
    start = i+1
   
    if  i == 3 :
        result.append("-1")
        break
    
    for j in range (start , size) : 
      
        if a[i] > max(a[start:]) :
            result.append("-1")
           

            break

        elif a[j] > a[i] : 
         
            tmp.append(a[j])

            if j == 3 :
                result.append(tmp[0])    
                tmp = []

print(" ".join(list(map(str,result))))
        
"""
import sys 
n = int(input())
answer = [None] *n
A = list(map(int,input().split()))
index_Stack = []

for i in range(n) : 
    while index_Stack and A[index_Stack[-1] ] < A[i] : #오큰수 조건
        answer[index_Stack.pop()] = A[i] #정답리스트에 오큰수 저장
    index_Stack.append(i)

while index_Stack : 
     answer[index_Stack.pop()] = -1

print(" ".join(list(map(str,answer))))


 