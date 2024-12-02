tmp = []

def go (index,first,second) : 
    if index == n :
        if len(first) != n//2:
            return 
        if len(second) != n//2:
            return 
        
        t1 = 0
        t2 = 0
        for i in range(n//2) : 
            for j in range(n//2) : 
                if i == j : 
                    continue
                t1 += a[first[i]][first[j]]
                t2 += a[second[i]][second[j]]

            diff = abs(t1-t2)
            tmp.append(diff)




        
        if len(first) > n//2:
            return 
        if len(second) > n//2:
            return 
        

        ans = -1
        t1 = go(index+1, first+[index], second)
        t2 = go(index+1, first, second+[index])
        return 






n = int(input())
a = [list(input().split())]
go(0, [], [])


