A,B = map(int,input().split())

def GCD(a,b) : 
    
    if b == 0 :
        return a 
    else : 
        return GCD(b,a%b)
    
def LCM (a,b,c) : 
    return int((a*b)/c)


print(GCD(A,B))
print(LCM(A,B,GCD(A,B)))

