def lower_bound(a,n,key) : #key보다 같거나 큰값중 가장 작은값
#여기서 보면 전체크기  n 에서 lowerbound를 가리키는 index를 찾는다 
#만약 그런 값이 없다면 비어있는 공간중 가장 앞부분을 가져온다
    left = 0 
    right = n 
    while left < right :
        mid = (left + right) //2
        if key <= a[mid] :
            right = mid
        else : 
            left = mid +1
    
    return left


n = int(input())
a = [0]*n
nums = list(map(int,input().split()))
length = 0 

for num in nums : 
    p = lower_bound(a,length,num)
    a[p] = num
    if length == p :  #그리고 이게 의미하는건 지금 만들어진 범위내에 모든 수가
        #꽉찼다는걸 의미하니깐 한칸 더 늘려줘야한다
        length +=1

print(length)