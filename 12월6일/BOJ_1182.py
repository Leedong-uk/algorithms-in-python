#부분집합을 구할떈 이렇게 구하자 길이가 계속 달라지니깐 이게 가장 편함
n,m = map(int,input().split())
a = list(map(int,input().split()))
ans = 0

def go(i, s): #i번쨰의 숫자를 추가할지말지 s는 i번째까지의 합 
    global ans
    if i == n:
        if s == m:
            ans += 1
        return
    go(i+1,s+a[i]) #i번쨰 숫자를 추가해 계산한다
    go(i+1,s) # i 번째  숫자를 추가하지않는다 


go(0, 0)


if m == 0:
    ans -= 1

print(ans)