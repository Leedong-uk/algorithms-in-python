
#t1 이 0으로 시작하는 애들 다 조사후 다시 t1이 1로시작하는 애들 다 조사
#재귀함수를 이해하려고 했더니 머리가 터질것 같음
#결국 이런 문제와 같이 t1에 추가할것이냐 t2에 추가 할것이냐 와 같은 문제는
#다음과 같이 t1에추가한경우 호출 t2에 초과한경우 호출 의 형태로 하면 다 구할수 있다는걸
#손코딩을 통해서 재귀함수 호출을 따라가 보면서 확인해 봤다 
#기존 코드를 내가 조금 바꿔봤다 솔직히 재귀 함수 호출만 생각해도 머리가 터질것 같아서 
# first팀과 second 팀의 길이가 n//2로 가득찬 경우에만 그 둘의 팀 시너지의 차를 tmp라는 배열에 저장하고 
#나중에 그 tmp의 최솟값을 찾으면된다
#여기서 중요한건 안되는 경우를 찾는것과 정답인 경우를 찾는경우를 명확하게 다 걸러줘야한다
#안되는 경우 :
#1.6번쨰 사람 즉 마지막 사람이 어느 팀에 들어 갈지 결정났는데 첫번쨰와 두번쨰 팀의 길이가 맞지 않는경우 return
#2. 마지막 사람까지 갈 필요도 없이 그냥 한쪽 길이가 n//2를 넘어가면 더 해볼필요없이 return
#정답인 경우 :
#모든 시너지를 더해서 그 둘의 차를 tmp에 저장하고 return 
#결과적으로 이 함수는 아무것도 return 하지 않게 되지만 tmp안에 그 값을 가져오게 된다 
#또하나 알게된점 여기서 index == n 일때 정답을 출력하게 되어있다 
#그러면 숫자는 n-1 까지 만 조사하게된다 범위를 조심하자 
tmp = [] 
def go(index, first, second):
    if index == n:
        if len(first) != n//2:
            return 
        if len(second) != n//2:
            return 
        t1 = 0
        t2 = 0
        for i in range(n//2):
            for j in range(n//2):
                if i == j:
                    continue
                t1 += s[first[i]][first[j]]
                t2 += s[second[i]][second[j]]
        diff = abs(t1-t2)
        tmp.append(diff)
        return 
    


    if len(first) > n//2:
        return 
    if len(second) > n//2:
        return 
    


    ans = -1
    t1 = go(index+1, first+[index], second)
    t2 = go(index+1, first, second+[index])
    return 




n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
go(0, [], [])

print(min(tmp))
