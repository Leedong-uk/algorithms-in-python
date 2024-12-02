"""""
import sys
start, end = map(int,sys.stdin.readline().split())
stack = [i for i in range(start,end+1)]
result = [] 
count = 0

if stack[0] == 1 : 
    stack.pop(0)
    

for i in stack : 
    if i > 1 : 
        for x in range(2,i+1) : 
            
            if i % x == 0 :
                count += 1

        if count == 1 : 
            result.append(i)

        count = 0            
    else : 
        continue

for i in range(len(result)) : 
    print(result[i])

"""
#*******************복습 꼭 하기 ************************************
#시간초과 났음 
#인터넷 검색해보니깐 에라토스테네스의 체 이게 나옴
#이 개념은 소수 문제를 풀떄 아주 유용함
#근데 이게 내가 맨처음 구현 할려고 했던 개념과 굉장히 똑같았음 
#다만 몰랐던 개념은 
#1.제곱근 까지 구해야 한다는점 
#2.처음에 원하는 수만큼 True로 초기화 시켜놓고 해당하는 값이 나오면 pop하는게 아니라 False로 차별점을 두는점
#위에 쓴 코드는 위 1,2번 개념이 없어서 구현하다 막혀 이전에 했던걸로 해볼려하다가 시간 초과가 났음
#에라토스테네스의 체 ->일정 범위 내 수열에서 배수들을 제거해 소수만 걸러내는 체
#에라토스테네스의 체 알고리즘 하는방법
#1.소수를 판별할 범위만큼 배열을 true로 초기화 시켜 만든다
#2.숫자 0과 숫자 1은 소수가아님으로 해당 stack[0] 과 stack[1]을 false 로만든다
#3.제곱근 까지 를 설정해주고 인덱스에 해당하는 value 값이 false면 그냥 무시한다
#4.만일 해당 인덱스 값이 true라면 그 수만큼 증가하면서 stack의 값을 false로만들자 이떄 시작하는 값은  *2로시작한다
#5.예를들어 i가 2라면 4부터 지워나가고 증가폭은 2(=i값)씩 증가해 false로만들자
#6.마지막에 true만 출력하면 끝 

start , end = map(int,input().split())

stack = [True] * (end+1)
stack[0] = False
stack[1] = False 

for i in range(2,int(end**0.5)+1) : 
    if stack[i]  : #이걸 왜 넣었나 생각해 봤는데 여기서 이미 체크해서 false로 만든 애들 한번더 계산 안할려고 하는거
        for j in range(i*2,end+1,i) : 
             stack[j] =False


for i in range(start,end+1) : 
    if stack[i] :
        print(i)