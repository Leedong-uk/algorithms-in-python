#이런식아닐까
#최소를 구하는거니깐 bfs고
#정수가 주어지면 그 정수가 갈수있는 모든 것을 q에 넣고
# 정수의 결과 값
#각 정수에 대해서 연산을 4번씩하면서 1.방문했는지 ,2.범위를 넘어가는지 조사
# q 에넣을떄  연산결과 x 값과 여태까지 어떤경로로 왔는지에 대한 s 입력 
# x가 t와 같아지면 종료
# x 의 크기가 0 이면 0으로 출력 
#평소처럼 check 의 배열을 통해 방문 여부를 했는데 메모리 초과가 떴다
#이럴떈 set를 이용해서 메모리 초과문제를 해결할수있다

from collections import deque
limit = 1000000001
s,t = map(int,input().split())
check = set()

q = deque()
q.append((s,''))
check.add(s)

while q : 
    x , s = q.popleft()
    if x == t : 
        if len(s) == 0 : 
            s = '0'
        print(s)  
        exit()
    
    if 0 <= x*x <= limit and x*x not in check:
        q.append((x*x,s+'*'))
        check.add(x*x)

    if 0 <= x+x <= limit and x+x not in check:
        q.append((x+x,s+'+'))
        check.add(x+x)

    if 0 <= x-x <= limit and x-x not in check:
        q.append((x-x,s+'-'))
        check.add(x-x)

    if x != 0 and 0 <= x//x <= limit and x//x not in check:
        q.append((x//x,s+'/'))
        check.add(x//x)

print(-1)


