def solution(info, edges):
    check=[False] *len(info)
    check[0] = True
    
    def dfs(sheep,wolf) : 
        if sheep == wolf : 
            return sheep
        max_sheep = sheep 
        
        for parent , child in edges : 
            if check[parent] and not check[child] : 
                check[child] = True
                
                if info[child] == 0 : 
                    max_sheep = max(max_sheep,dfs(sheep+1,wolf))
                else : 
                    max_sheep = max(max_sheep,dfs(sheep,wolf+1))

                check[child] = False
        return max_sheep
        

    return dfs(1, 0)