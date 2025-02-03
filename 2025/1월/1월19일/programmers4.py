from itertools import permutations
dungeons = [[78, 18], [70, 11], [67, 9], [60, 8], [59, 2], [57, 54]]

for i in range(len(dungeons),0,-1) : 
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡ',i,'번 순열','ㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    permu_case = list(permutations(dungeons,i))
    for permu_set in permu_case : 
        health = 78 # == k 
        cnt = 0
        check = True
        for j in permu_set : 
            if j[0]>health :
                check = False
                break
            health -=j[1]
            cnt +=1
        
        if check :
            break
    
    if check : 
        break


print(cnt)