n = int(input()) #비트마스크로 풀어보자 1번팀에 들어가면 1 2번팀에 들어가면 0 이런식으로 나눌수 있기때문에
s = [list(map(int,input().split())) for _ in range(n)]
ans = -1

for i in range((1<<n)):
    
    first = []
    second = []

    for j in range(n): #만들어진 부분집합속에서 1번팀에 들어가있으면 검색 했을떄 0보다 크게 나올꺼임 
        if (i&(1<<j)) > 0: # 0보다 크다 ? 해당 비트가 1이 라는뜻 즉 fist팀에 들어 가있단 뜻임
            first += [j] #이걸 한 부분집합에대하여 팀가르기를 계속할수있겠지
        else:
            second += [j] # 맞지 그러면 여기까지했으면 일단은 한 경우의 부분집합에대하여 first 와 second로 다 나눠본거야
    
    if len(first) != n//2:  #그리고 팀의 분배가 올바르게 되지않은놈들을 싹다 걸러냄
        continue


    t1 = 0
    t2 = 0
    #여기까지 왔다는건 부분집합 애들중 first와 second 다 알맞게 분배 되어있는 애들을 가지고 온거임 
    #그럼 밑에는 이제 똑같지 

    for l1 in range(n//2):
        for l2 in range(n//2):
            if l1 == l2:
                continue
            t1 += s[first[l1]][first[l2]]
            t2 += s[second[l1]][second[l2]]
    diff = abs(t1-t2)
    if ans == -1 or ans > diff:
        ans = diff
print(ans)
