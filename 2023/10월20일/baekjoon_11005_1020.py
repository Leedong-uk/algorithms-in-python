import sys
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

a,b = map(int,sys.stdin.readline().split())

result=""

while a !=0 :
    x=a%b  
    result = arr[x] + result
    a = a//b

print(result)