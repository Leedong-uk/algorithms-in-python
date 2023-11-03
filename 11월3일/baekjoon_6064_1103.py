#우리가 구해야하는건 k임
#일단 M=10 N=12 X=3 Y=9 K=33으로 예시를 둬보자
# (K-X)%M = 0 (K-Y)%N = 0  을 만족한다 
#그러면 K를 찾을떄 이걸 이용을 하면된다 
#그렇다고 1부터 하나씩 늘려서 찾는것이 아님
# K-X 는 M의 배수 즉 K =X -> K = X+M -> K=X+2M 이런식으로간다
#이는 K-Y도 마찬가지 즉 둘중 하나만을 이용해서 K값을 증가시키면됨
#여기선 K-X를 이용할거고 ->K를 X로 초기화하고 M을 더해가면 된다
import sys

def cal (m,n,x,y):
    k = x #k를x로 초기화
    while k<= m*n : #k의 범위는 m*n을 넘을수 없다
        if (k-x)%m == 0 and (k-y) % n ==0 : 
            return k
        k +=m

    return -1

N =int(input())    
for _ in range(N) : 
    m , n ,x, y = map(int,sys.stdin.readline().split())

    print(cal(m,n,x,y))