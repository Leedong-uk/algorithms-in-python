def next_permutation(a) : 
    i = len(a) -1
    while i >0 and a[i-1] >=a[i] : #순열에서 i를 찾기위한과정 (1번과정)
        i-=1
    if i <=0 :      #이건 순열의 가장 마지막 즉 처음부터 끝까지 모두 내림차순으로  된경우를 의미함
        return False
    
    j = len(a)-1
    while a[j] <= a[i-1] : #a[j] >=a[i-1]을 만족하는 가장 큰 j를 찾는다 현재 내림차순이여서 저걸 만족하는
        j -=1              #가장 마지막 값을 찾으면 그값이 가장 큰 j 값이 된다 (2번과정)


    a[i-1],a[j]  = a[j],a[i-1]   #(3번과정)

    j = len(a)-1
    while i <j :                #(4번과정)
        a[i],a[j] = a[j],a[i]
        i+=1
        j-=1

    return True





n = int(input())
a = list(map(int,input().split()))

if next_permutation(a) : 
    print(" ".join(map(str,a)))
else :
    print(-1)