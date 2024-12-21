def solution(board,moves):
    result = 0
    basket = []
    n = len(board)
    for i in moves : 
        for j in range(n) : 
            if board[j][i-1] != 0 : 
                basket.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(basket) >=2 and basket[-1] == basket[-2] : 
            result +=1
            del basket[-1:-3:-1]
    
    return result*2

