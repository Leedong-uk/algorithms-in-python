lst = []
tmp = 0

for _ in range(9) : 
    lst.append(int(input()))

lst.sort()

total = sum(lst)

for i in range(9) : 
    for j in range(9) : 
        if total - (lst[i]+lst[j]) == 100 : 
           x , y = lst[i] ,lst[j]
           break

lst.remove(x)
lst.remove(y)


for i in lst :
    print(i)  