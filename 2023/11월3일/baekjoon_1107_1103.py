#이 문제에서 내가 잘못된점은 브루트 포스 즉 0부터 쭈우욱 모든 수를 다 검사하면 된다
#그리고 맨처음 채널을 누르는 버튼수는 부서진 버튼이 없는 완전한 수의 길이이며
#+-로 이동할떄의 버튼수는 목표로하는수 - 현재수 를 뺸 차이만큼 +하든 -하든 하면된다
#즉 abs로 해도 상관이 없다는것!

n = int(input())
m = int(input())
broken = [False] * 10
if m > 0:
    a = list(map(int,input().split()))
else:
    a = []
for x in a:
    broken[x] = True
def possible(c):
    if c == 0:
        if broken[0]:
            return 0
        else:
            return 1
    l = 0
    while c > 0:
        if broken[c%10]:
            return 0
        l += 1
        c //= 10
    return l
ans = abs(n-100)
for i in range(0, 1000000+1):
    c = i
    l = possible(c)
    if l > 0:
        press = abs(c-n)
        if ans > l + press:
            ans = l + press
print(ans)



