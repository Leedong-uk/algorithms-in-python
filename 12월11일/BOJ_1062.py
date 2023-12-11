# (1<<26)-1 의 의미 알파벳은 26개인데  int는 32비트다 즉 그냥 ~mask를 해버리면 앞에 6자리는 1이 남는다
#그래서 그냥 11111 26개를 가지는 비트를 만들기 위해서 만든거다
#그냥 1이 26개 있는걸 만들기위해서 저렇게 연산함 1111111111111111111111111111111111111111111
#거기서mask(배운알파벳)를 뺴면 배우지 않은 애들이 나오게 되고
#그게 지금 word 에있는지 비교해서 0이나오면 없다는 뜻이고 1이나오면  배우지 않은 애들이 존재한다는 뜻이된다
def count (mask,words) :
    #우리가 비교 할건 문제에서 주어진 단어가 우리가 고른 단어 mask 와 비교하여
    # mask에 없는 값을 가지고 있는지 아닌지를 확인한다  
    cnt = 0
    for word in words : 
        if (word & ((1<<26)-1-mask)) == 0:
            # (1<<26)-1 의 의미 알파벳은 26개인데  int는 32비트다 즉 그냥 ~mask를 해버리면 앞에 6자리는 1이 남는다
            #그래서 그냥 11111 26개를 가지는 비트를 만들기 위해서 만든거다
            #그냥 1이 26개 있는걸 만들기위해서 저렇게 연산함 1111111111111111111111111111111111111111111
            #거기서mask(배운알파벳)를 뺴면 배우지 않은 애들이 나오게 되고
            #그게 지금 word 에있는지 비교해서 0이나오면 없다는 뜻이고 1이나오면  배우지 않은 애들이 존재한다는 뜻이된다
            cnt +=1
    
    return cnt

def go (index , k ,mask,words) : 
    if k < 0 : 
        return 0
    
    if k ==26 : 
        return count(mask,words)
    
    ans = 0 
    t1 = go (index+1,k-1,mask| (1<<index),words)
    if ans < t1 : 
        ans = t1
    if index not in [ord('a')-ord('a'), ord('n')-ord('a'), ord('t')-ord('a'), ord('i')-ord('a'), ord('c')-ord('a')]:
        #antic는 무조건 포함해야하니깐 이걸 무조건 포함시켜야할 방법이 필요했다
        #그 방법으로 우리가 제귀함수를 통한 브루투 포스를 돌릴때 index번쨰것을 포함 하는경우의 함수와 포함 하지않는 경우함수
        #두개의 함수로 돌린다 이떄 포함하지않는 함수를 그대로 가져다 쓰는게아니라
        #꼭 포함되어야 하는 애들에 순서에 대해선 포함되지않는 함수가 돌아가지 않게 만든다 
        t2 = go(index+1, k, mask, words)
        if ans <t2 : 
            ans = t2
    
    return ans
    






n , m = map(int,input().split())
words = [0]*n 
for i in range(n) : 
    s = input()
    for x in s : 
        #i번쨰 단어가 가지고있는 알파벳을 word[i]에 비트마스크로 넣는다 
        words[i] |= (1 << (ord(x)-ord('a')))
        
print(go(0,m,0,words))