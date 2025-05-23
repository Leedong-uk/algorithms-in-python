n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
result = 0 
linked_list = [[] for _ in range(n+1)] 
check = [False] *(n+1)
temp = [0] * (n+1)

for i in wires : 
    x,y = i 
    linked_list[x].append(y)
    linked_list[y].append(x)
    
def dfs(curr,parent) : 
    check[curr] = True
    cnt = 1
    
    for next in linked_list[curr] : 
        if next == parent : 
            continue
        
        if check[next] == False :
            cnt +=dfs(next,curr)
    temp[curr] = cnt
    return cnt

dfs(1,None)
result =min((map(lambda x: abs(n - 2 * x), temp)))
print(result)
    
    

