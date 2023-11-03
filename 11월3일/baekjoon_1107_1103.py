#이 문제에서 내가 잘못된점은 브루트 포스 즉 0부터 쭈우욱 모든 수를 다 검사하면 된다
#그리고 맨처음 채널을 누르는 버튼수는 부서진 버튼이 없는 완전한 수의 길이이며
#+-로 이동할떄의 버튼수는 목표로하는수 - 현재수 를 뺸 차이만큼 +하든 -하든 하면된다
#즉 abs로 해도 상관이 없다는것!

n = int(input())
m = int(input())
broken = [False]*10

#check method 초기화
def check(x) : 
    count = 0
    for i in x : 
        
        if broken[int(i)] : 
            return 0
        
        else: 
            count+=1

    return count        
        

if m > 0:
    a = list(map(int,input().split()))
    #부숴진 버튼 체크
    for i in a : 
        broken[i] = True

    ans = abs(n-100)        


    for i in range(1000001) : 
        c = str(i)
        k = check(c)
        if k > 0 :
            press = abs(n-i)
            if ans > k + press:
                ans = len(c)+press

    print(ans)    

elif  m == 0 :
    if n == 100:
        print(0)
    else : 
        print(len(str(n)))



