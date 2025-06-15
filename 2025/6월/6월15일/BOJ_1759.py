L , C = map(int,input().split())
mo = "aeiou"
alpha = input().split()
alpha.sort()
result = []

def dfs(start,depth,temp) : 
    if depth == L : 
        mo_cnt = sum(1 for i in temp if i in mo)
        ja_cnt = L-mo_cnt
        
        if mo_cnt >=1 and ja_cnt >=2 : 
            print(temp)

        return
    
    for i in range(start,len(alpha)) : 
        dfs(i+1,depth+1,temp+alpha[i])

dfs(0,0,"")


                