def solution(info, edges):
    max_sheep = 0
    # 여기 틀렸어요 
    check = [False] * (len(info) + 1)
    check[0]=0
    
    def dfs(curr,sheep,wolf) : 
        max_sheep = sheep
        
        if sheep == wolf : 
            return sheep 

        for parent , child in edges : 
            if check[parent] and not check[child] : 
                #여기 틀렸어요
                check[child] = True

                if info[child] ==  0 :
                    #여기도 틀렸어요
                    max_sheep = max(max_sheep,dfs(curr,sheep+1,wolf))
                else : 
                    max_sheep = max(max_sheep,dfs(curr,sheep,wolf+1))
        
                check[child] = False
        return max_sheep
            
    
    return dfs(1, 0)




print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))