#모든 부분수열 구하고
#각각의 부분수열이 포함하고있는 숫자 구하고 
#그 숫자를 더한값을 check 에 true 로만들고
#check 에서 false로 된것중 가장 작은거 출력하면됨 

n = int(input())
a = list(map(int,input().split()))
c = [False]*(n*100000+10) 
for i in range(1<<n) :  #인덱스를가지고 부분수열을 만듬 
    #비트마스크에서 s = [0 ~ n-1] (총원소의 갯수 = n ) 일때  전체집합은 (1<<n)-1
    #이떄 1011 이러면 s[0]s[2]s[3] 숫자가 포함된 부분순열이란 뜻
    s = 0 
    for j in range(n) : 
        if (i &(1<<j)) : 
            s += a[j]
    
    c[s] = True 

i=1
while True : 
    if c[i] == False : 
        break
    i+=1

print(i)
