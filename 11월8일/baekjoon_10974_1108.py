"""from itertools import permutations

n = int(input())
num = [i for i in range(1,n+1)]
p_num  = permutations(num)

for i in p_num : 
    print(" ".join(map(str,i)))

"""
def all_permutation(a) : 
    i = len(a) -1
    while i >0 and a[i-1] >=a[i] : 
        i-=1
    if i <=0 :    
        return False
    
    j = len(a)-1
    while a[j] <= a[i-1] : 
        j -=1              


    a[i-1],a[j]  = a[j],a[i-1]   

    j = len(a)-1
    while i <j :               
        a[i],a[j] = a[j],a[i]
        i+=1
        j-=1

    return True



n = int(input())
a = [i for i in range(1,n+1)]

while True : 
    print(" ".join(map(str,a)))
    if all_permutation(a) == False : 
        break
    


 
    