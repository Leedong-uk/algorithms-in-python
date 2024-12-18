n = int(input())
a = list(map(int,input().split()))
m = int(input())
num = list(map(int,input().split()))


a.sort()

for i in num : 
    l = 0
    r = n-1
    while True : 
        mid = (l+r) // 2
        if i == a[mid] : 
            print(1)
            break 
        elif l >= r : 
            print(0)
            break
        elif a[mid] < i :
            l = mid+1
        else : 
            r = mid-1




            
