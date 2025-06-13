def solution (numbers) : 
    numbers_list = set()
    check = [False] * len(numbers)
    
    
    
    def dfs(end,path) : 
        if len(path) == end : 
            num = int(''.join(path))
            numbers_list.add(num)
            return 
        
        for i in range(len(numbers)) : 
            if not check[i] : 
                check[i] = True
                dfs(end,path+[numbers[i]])
                check[i] = False
        
        
    for end in range(1,len(numbers)+1) : 
        dfs(end,[])
    
    n = max(numbers_list)
    board = [True] * (n+1)
    board[0] = False
    board[1] = False
    
    for i in range(2,int(n**0.5)+1) : 
        for j in range(i*i,n+1,i) : 
            board[j] = False
    
    cnt = 0
    for i in numbers_list : 
        if board[i] ==True : 
            cnt +=1
    
        
    return cnt




print(solution("17"))
print(solution("011"))

