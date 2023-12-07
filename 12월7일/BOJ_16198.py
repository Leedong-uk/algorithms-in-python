n = int(input())
w = list(map(int,input().split()))


def go (a) : 
    m = len(a)

    if m == 2 : 
        return 0
    
    ans = 0
    for i in range(1,m-1) : 
        energy =  (a[i-1] * a[i+1])
        b = a[:i] + a[i+1:]
        x = go(b)
        energy += x

        if ans < energy : 
            ans = energy


    return ans 

print(go(w))


