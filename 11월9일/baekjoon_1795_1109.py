import sys
m,n = map(int,input().split()) #정답 배열 m 
alpha = list(map(str,input().split()))
alpha.sort()
c= [False]*n
ans = [0]*m
k = ['a','e','i','o','u']
tmp = []

def check(password):
    ja = 0
    mo = 0
    for x in password:
        if x in 'aeiou':
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1


def go(index, start,n, m):
    if index == m :
        if check(ans) :  
            tmp.append(tuple(ans))
        return 
   
    
    
    for i in range(start , n):
        if c[i]:
            continue
        c[i] = True
        ans[index] = alpha[i]
        go(index+1, i, n, m)
        c[i] = False

go(0,0,n,m)
tmp = list(set(tmp))
tmp.sort()

for i in tmp : 
    print("".join(map(str,i)))