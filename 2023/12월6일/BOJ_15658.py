from itertools import permutations
n = int(input())
a = list(map(int,input().split()))
op_num = list(map(int,input().split()))
op = ['+','-','*','/']
pocket = []
pocket_2 = []
tmp = ""
result = ''



def calc(tmp,a,pocket_2) : # k는 순서  k 순서대로 호출함  
    for i in range(len(pocket_2)) : 
        ans = a[0]
        for j in range(len(pocket_2[i])) :
            if tmp[(pocket_2[i][j])] == "+" : 
                ans = ans + a[j+1]

            if tmp[(pocket_2[i][j])] =='-' :
                ans = ans - a[j+1]
               
            if tmp[(pocket_2[i][j])] == '*' : 
              
                ans = ans * a[j+1]  
               
    
            if tmp[(pocket_2[i][j])] == '/' : 
             
                if ans > 0:
                    ans = ans // a[j+1]
                  
                else :
                    ans = -(-ans // a[j+1])
                   

        pocket.append(ans)
    return ans 


tmp =''
for i in range(4) : 
    tmp += op[i]*op_num[i]
tmp_num = [i for i in range(len(tmp))]

pocket_2 = list(permutations(tmp_num,4))
print("만들어진 순서쌍 : ",end =' ')
print(pocket_2)
calc (tmp,a,pocket_2)


print(max(pocket))
print(min(pocket))
#-------------------------------------------------------