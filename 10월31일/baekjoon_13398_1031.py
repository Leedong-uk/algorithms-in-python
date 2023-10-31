# L[i] : L2R 왼쪽에서 i를 포함한 연속의 최대값 ->그전에 있는 연속된 수에 i를 붙여 이어갈것인가? , 아니면 i부터 새로시작할것인가
# R[i] : R2L 오른에서 i를 포함한 연속의 최대값 ->그전에 있는 연속된 수에 i를 붙여 이어갈것인가? , 아니면 i부터 새로시작할것인가
# L[i-1] + R[i+1]의 최대값을 찾는다 그러면 자연스럽게 i번쨰는 제거한 값이 된다

N = int(input())
A = list(map(int,input().split()))

L = [0]*(N)
L[0] = A[0]

R = [0]*(N)
R[N-1] = A[N-1]

result = 0

for i in range(1,N) : 
    L[i] = max(A[i],L[i-1]+A[i])
    R[N-1-i] = max(A[N-1-i],R[N-1-i+1]+A[N-1-i])

for i in range(1,N-1) : 
    tmp = int(L[i-1]+R[i+1])
    result = max(result,tmp)

print(L)
print(R)
print(result)