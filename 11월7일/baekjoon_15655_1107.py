n , m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()

check = [False]*n          #n으로 왜 할까 n = 선택가능한 자연수 수임 
ans = [0]*m              #예를들어 4 5 2 가 입력되면 sort를 통해 2 4 5 로 바뀌고 

def go (index,start,n, m ) : 
    if index == m : 
        print(" ".join(map(str,ans)))
        return

    for i in range(start, n ) : 
        if check[i] :  #어차피 주어진 수안에서 하면 이거 필요 없지않음? 아님
            continue   #이건 중복을 없애기 위해서 넣은거임 

        check[i] = True 
        ans[index] = num[i]
        go(index+1,i+1,n,m)
        check[i] = False


go(0,0,n,m)