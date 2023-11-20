tmp = [] 
def go (index, first , second ) : 
    #정답을 맞춘경우
    if index == n :
        if len(first) == 0 :
            return
        if len(second) == 0 :
            return
    
        t1 = 0
        t2 = 0 

        for i in first:
            for j in first : 
                if i == j : 
                    continue
                t1 += s[i][j]
    
        for i in second:
            for j in second : 
                if i == j : 
                    continue
                t2 += s[i][j]
    
        diff = abs(t1-t2)
        tmp.append(diff)
        return 
    
    t1 = go (index+1,first+[index],second)
    t2 = go(index+1,first,second+[index])
    return


n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
go(0, [], [])

print(min(tmp))
    
                 

