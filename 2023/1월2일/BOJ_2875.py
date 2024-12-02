n,m,k = map(int,input().split())

count = 0 

while True : 
    n -=2
    m -=1
    if n <0 or m<0 or (n+m) <k : 
        break
    count +=1
print(count)