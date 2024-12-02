n = int(input())

def fac(a) : 
    if a == 1 : 
        return 1
    elif a == 0 :
        return 1
    else : 
        return a * fac(a-1) 



print(fac(n))

