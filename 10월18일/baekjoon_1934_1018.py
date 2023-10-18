import math 
n = int(input())
result = []


def gcd (a,b): 
    if b == 0 :
        return a
    else : 
        return gcd(b,a%b)
    

for _ in range(n) : 
    a,b = map(str,input().split())
    if a.isdigit() and b.isdigit() : 
        a= int(a)
        b = int(b)
        result.append(int(a*b/gcd(a,b)))
    else : 
        pass


for i in range(len(result)) : 
    print(result[i])


"""""
import math 
n = int(input())
result = []
for _ in range(n) : 
    a,b = map(str,input().split())
    if a.isdigit() and b.isdigit() : 
        result.append(math.lcm(int(a),int(b)))
    else : 
        pass


for i in range(len(result)) : 
    print(result[i])
    """