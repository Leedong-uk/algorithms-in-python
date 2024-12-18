score = [10,100,20,150,1,100,200]
k = 3
answer = []
honor = []

for i in range(k) : 
    honor.append(score[i])
    answer.append(min(honor))
    print("answer값:",answer)

for j in range(k,len(score)) : 
    if min(honor) < score[j] : 
        print("----------------------------------------")
        print("현재들어온값 : ",score[j])
        index = honor.index(min(honor))
        print("honor에 최소값 :", min(honor) ," , 인덱스위치 : " ,index)
        honor[index] = score[j]
        print("변경후값:",honor)
        answer.append(min(honor))
        print("answer값:",answer)
        