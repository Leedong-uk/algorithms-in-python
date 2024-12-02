import math
import sys
n = int(input())
result = 0

for _ in range(0,n) : 
    arr=list(map(int,input().split()))
    arr.pop(0)
    result = 0
    for i in range(len(arr)) : 
        for j in range(i+1,len(arr)) : 
            x = math.gcd(arr[i],arr[j])
            result +=x
    
    print(result)



    

