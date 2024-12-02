n = int(input())
r = [0 for i in range(n)]

b = list(map(int,input().split()))

r[0] = b[0]
for i in range (1,n) : 
    r[i] = b[i]*(i+1) - (sum(r[:i]))

for i in r :
    print (i,end=" ")