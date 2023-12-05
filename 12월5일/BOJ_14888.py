n = int(input())
a = list(map(int,input().split()))
op_num = list(map(int,input().split()))
op = ['+','-','*','/']
pocket = []


def next_permutation(a) : 
    i = len(a)-1

    while i>0 and a[i-1] >=a[i] : 
        i -=1
    
    if i <=0 : 
        return False
    
    j = len(a)-1

    while a[j] <=a[i-1] :
        j -=1

    a[i-1],a[j] = a[j],a[i-1] 

    j= len(a)-1

    while i < j : 
        a[i],a[j] = a[j],a[i]
        i+=1
        j-=1

    return True



def calc(tmp,a,k) : # k는 순서  k 순서대로 호출함  
    ans = a[0] 
    for i in range(len(k)) : 
        if tmp[k[i]] == "+" : 
            ans = ans + a[i+1]
    
        if tmp[k[i]] =='-' : 
            ans = ans - a[i+1]

        if tmp[k[i]] == '*' : 
            ans = ans * a[i+1]    
    
        if tmp[k[i]] == '/' : 
            if ans > 0:
                ans = ans // a[i+1]
            else :
                ans = -(-ans // a[i+1])
    
    return ans 


tmp =''
for i in range(4) : 
    tmp += op[i]*op_num[i]

tmp_num = [i for i in range(len(tmp))]


while True : 
    x = calc(tmp,a,tmp_num)
    pocket.append(x)

    if not next_permutation(tmp_num):
        break

print(max(pocket))
print(min(pocket))
#-------------------------------------------------------