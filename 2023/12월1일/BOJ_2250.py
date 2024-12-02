import sys
sys.setrecursionlimit(200000)

n = int(input())
a = dict()
left = [0]*(n+1)
right = [0]*(n+1)
cnt = [0]*(n+1)
order = 1  #노드의 추가될 열

class Node : 
    depth = 1
    row = 0
    def __init__(self,left,right) :
        self.left = left
        self.right = right

#인오더 구현         
def inorder (node,depth) : #왼쪽 노드 오른쪽
    if node == -1 : 
        return
    inorder(a[node].left,depth+1)
    global order 
    a[node].row = order
    order +=1
    a[node].depth = depth
    inorder(a[node].right,depth+1)

for _ in range(n) : 
    x ,y, z = map(int,input().split())
    if y != -1 : 
        cnt[y] +=1
    if z != -1 : 
        cnt[z] +=1
    
    a[x] = Node(y,z)


#루트 찾기
root = 0
for i in range(1,n+1) : 
    if(cnt[i]== 0 ) : 
        root = i

inorder(root,1)
maxdepth = 0
for i in range(1,n+1) : 
    depth = a[i].depth  #각 노드들의 깊이와
    order = a[i].row    #열값을 모두 가져옴 
    if(left[depth]== 0 ) : #그리고 left라는 배열이 비어있으면 일단 채워 넣음
        left[depth] = order 
    else : 
        left[depth] = min(left[depth],order) #left배열에 값이 있을경우 값을 비교해서 작은값을 채워넣음 
                                             # 이떄 index 는 depth를 가리키고있어서 하나의 depth 에 속한 애들중 최소값을 찾게됨
    right[depth] = max(right[depth],order) # 하나의 depth 에 속한 애들중 row의 최대값을 찾게됨
    maxdepth = max(maxdepth,depth) # 각 depth마다의 최대 너비를 비교하기 위해서 깊이의 최대값을 구하고 그만큼 반복문을 돌릴꺼임

ans = 0 
ans_level = 0 
for i in range(1,maxdepth+1) : 
    if(ans < right[i]-left[i]+1) : 
        ans = right[i]-left[i]+1
        ans_level = i

print(ans_level,ans)

