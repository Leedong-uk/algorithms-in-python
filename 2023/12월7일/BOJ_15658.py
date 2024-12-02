'''from itertools import permutations

def calc(order,tmp,a) : 
    for i in range (len(order)) : 
        ans = a[0]
        for j in range(len(order[i])) : 

            if tmp[order[i][j]] == "+" :
                ans = ans + a[j+1]
            
            if tmp[order[i][j]] == '-' : 
                ans = ans - a[j+1]
            
            if tmp[order[i][j]] == '*' :
                ans = ans*a[j+1]
            
            if tmp[order[i][j]] == '/' : 

                if ans >0 : 
                    ans = ans // a[j+1]
                
                else :
                    ans = -(-ans //a[j+1]) 
        
        pocket.append(ans)
            
        




n = int(input())
a = list(map(int,input().split()))
op_num = list(map(int,input().split()))
op = ['+','-','*','/']
pocket = []


tmp =''

for i in range(4) : 
    tmp += op[i]*op_num[i]

tmp_num = [i for i in range(len(tmp))]  
order = list(permutations(tmp_num,n-1))  


calc(order,tmp,a)
print(max(pocket))
print(min(pocket))'''


def calc(a, index, cur, plus, minus, mul, div):
    if index == len(a):
        return (cur, cur)
    res = []
    if plus > 0:
        res.append(calc(a,index+1,cur+a[index],plus-1,minus,mul,div))
    if minus > 0:
        res.append(calc(a,index+1,cur-a[index],plus,minus-1,mul,div))
    if mul > 0:
        res.append(calc(a,index+1,cur*a[index],plus,minus,mul-1,div))
    if div > 0:
        if cur >= 0:
            res.append(calc(a,index+1,cur//a[index],plus,minus,mul,div-1))
        else:
            res.append(calc(a,index+1,-(-cur//a[index]),plus,minus,mul,div-1))
    ans = (
        max([t[0] for t in res]),
        min([t[1] for t in res])
    )

    return ans

n = int(input())
a = list(map(int,input().split()))
plus,minus,mul,div = map(int,input().split())
ans = calc(a, 1, a[0], plus, minus, mul, div)
print(ans[0])
print(ans[1])








