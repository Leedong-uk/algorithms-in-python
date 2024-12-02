def prev_permutation(a) : 
    #1번과정
    i = len(a)-1            
    while i>0 and a[i] >= a[i-1] :  
        i -=1
    if i <=0 :      
        return False
    
    #2번과정
    j = len(a)-1
    while a[j] >= a[i-1] :
        j-=1

    #3번과정
    a[i-1],a[j]  = a[j],a[i-1]

    #4번과정
    j = len(a) -1
    while i<j : 
        a[i],a[j] = a[j],a[i]
        i+=1
        j-=1

    return True

    



n = int(input())
a = list(map(int,input().split()))

if prev_permutation(a) : 
    print(" ".join(map(str,a)))
else :
    print(-1)