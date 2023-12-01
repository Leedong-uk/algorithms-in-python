class Node : 
    def __init__ (self,left,right) : 
        self.right = right
        self.left = left

#클래스는 여기까지
#클래스는 단순히 트리를 구현하기위해서 만 만들었음 
        

def preorder(x) : #프리오더 : 노드방문 ->왼쪽프리오더 ->오른쪽 프리오더
    if x == -1 :  #??? 이건 왜한거지
        return
    print(chr(x+A),end = '')
    preorder(a[x].left)
    preorder(a[x].right)

def inorder(x) :  #인오더 : 왼쪽인오더 ->노드방문 ->오른쪽인오더
    if x == -1 : 
        return
    inorder(a[x].left)
    print(chr(x+A),end="")
    inorder(a[x].right)


def postorder(x) : #포스트오더 : 왼쪽포스트오더->오른쪽포스트오더 ->노드방문
    if x == -1 : 
        return
    inorder(a[x].left)
    inorder(a[x].right)
    print(chr(x+A),end = "")

n = int(input())
a = dict()
A = ord('A')

for _ in range(n) : 
    x,y,z = input().split()
    x = ord(x)-A #아스키 코드를 이용하는것
    left = -1
    right = -1
    if y != "." : #.이들어오면 -1이 유지되고 -1이 유지되면 아무것도 안함 
        left = ord(y)-A
    if z!= "." : 
        right = ord(z)-A
    a[x] = Node(left,right) #트리를 저장함
                            #이걸 모르겠음 노드 class의 오브젝트를 왜 dictionary에 저장해 ?
                            #a 의 x번쨰는 node class의 객체다 
                            #클래스와 딕셔너리는 관련이 엄청있음
                            #사용자 정의 객체도 인스턴스 데이터와 클래스를 위해 딕셔너리를 사용한다. 
                            #사실, 객체 시스템 대부분이 딕셔너리 위에 세워진 추가적인 계층이라 할 수 있다.
                            #해당 인스턴스에 . __dict__ 라고 치면 
                            #인스턴스의 데이터들을 볼수있다 여기선 left : right : 이런식으로
                            #어떻게 저장되는지 궁금하면 아래의 주석처리를 풀고 실행해봐라

    """print("a[%d] 의 모습 : "%x,end= " ")
    print(a[x].__dict__)"""

#정확히는 클래스를 통해 각 노드의 대해서 left와 right 관계만 저장해두고
#위에서 만든 각각의 관계들을 a라는 dictionary에 모든 node 인스턴스를 저장하여 
#나중에 필요시 해당 index에있는 인스턴스를 호출하기 편하게 해준다 
preorder(0)
print()
inorder(0)
print()
postorder(0)
print()