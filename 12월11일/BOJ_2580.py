def check(row, col):
    if check_col[col]: #COL 열에 퀸이 있다면 True 
        return False
    if check_dig[row+col]: # 대각선에 퀸이 있다면 True
        return False
    if check_dig2[row-col+n-1]: #반대 대각선에 퀸이 있다면 true
        return False
    return True

def calc(row):
    if row == n: #n개를 놓을수 있는 방법의 수는 1개뿐
        return 1
    ans = 0
    for col in range(n):
        if check(row,col): #check로 걸렀는데 살아남았다면
            check_dig[row+col] = True 
            check_dig2[row-col+n-1] = True
            check_col[col] = True
            a[row][col] = True #다 true로 만들어주고
            ans += calc(row+1) #다음꺼 실행
            check_dig[row+col] = False 
            check_dig2[row-col+n-1] = False
            check_col[col] = False
            a[row][col] = False
    return ans

n = int(input())
a = [[False]*n for _ in range(n)]
check_col = [False] * n
check_dig = [False] * (2*n-1)
check_dig2 = [False] * (2*n-1)
print(calc(0))
