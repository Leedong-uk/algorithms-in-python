#내가 확실하게 정할수 있는건 마지막의 모습이다
#1. 끝나는 모양이 마지막 2잔을 연속해서 먹는경우 ~~~~ MAX + X O O 
#2. 끝나는 모양이 1잔을 먹을건데 마지막에 먹는경우~~~~~~~ MAX X O
#->마지막에 확실히 먹을려면 앞에 X 가있어야한다 안그러면 연속해서 먹을수도 있기 때문에 
#3. 끝나는 모양이 1잔을 먹을건데 마지막에 먹지않는경우~~~~~~ MAX X  

N = int(input())

wine = []

for i in range(N) : 
    wine.append(int(input()))

d = [0]*N

d[0] = wine[0]

if N >1 : 
    d[1] = wine[0] +wine[1]

if N>2 : 
    d[2] = max(wine[2]+wine[1],wine[2]+wine[0],d[1])

for i in range(3,N) : 
    d[i] = max(d[i-1],d[i-3]+wine[i-1]+wine[i],d[i-2]+wine[i])


print(d[N-1])
