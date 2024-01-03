# b에있는 숫자 하나하나가 a에 있는 지 확인 


def b_search (a,num) : 
    left = 0
    right = len(a) -1
    ans = -1

    while left <= right :
        mid = (left+right) // 2 

        if  a[mid] == num : 
            return True
        
        elif a[mid] > num : 
            right = mid -1 
        
        else : 
            left = mid +1 
    
    return False 


n = int(input())
a = list(map(int,input().split()))
a.sort()
m = int(input())
nums = list(map(int,input().split()))

for num in nums : 
    tmp = b_search(a,num)
    if tmp  : 
        print(1,end=' ')
    else :
        print(0,end=' ')