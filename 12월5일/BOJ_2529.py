n = int(input())
boo = list(map(str,input().split()))
tmp = []
check = [False]*(11)
ans = [0]*(n+1)

def m_check(ans,x) :  #ans를 검사한다 , x: 기호의 개수
    for i in range(x) : 
        if boo[i] == ">" :
            return ans[i] > ans[i+1]
        
        if boo[i] =='<' : 
            return ans[i] < ans[i+1]
    


def go(index,x) : #index자리에 숫자넣음  , x  : 기호의 개수
    if index == x+1 : 
        if m_check(ans,x) : 
            t = "".join(map(str,ans))
            tmp.append(t)
            return
        return
    
    for i in range(10) : 
        if check[i] == True :
            continue

        check[i] = True
        ans[index] = i
        go(index+1,x)
        check[i] = False
        

go(0,n)
tmp.sort()
print(tmp[-1])
print(tmp[0])




