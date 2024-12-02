n = int(input())
p = list(map(int,input().split()))
p.sort()
a = [0]*n
a[0] = p[0]
ans = 0 

for i in range(1,len(p)) : 
    a[i] = a[i-1]+p[i]

for i in a : 
    ans +=i

print(ans)



