def solution(mats, park):
    mats.sort(reverse = True)
    mats_check = [False] *(max(mats) + 1) 

    for mat_size in mats : 
        found = False
        for i in range(len(park)) :
            if found : 
                break
            for j in range(len(park[0])) : 
                if found : 
                    break

            #i,j에서 메트크기만큼 정사각형 조사
                can_place = True
                for k in range(mat_size) :
                    if can_place == False :
                        break
                    for l in range(mat_size) : 
                        dx,dy = i+k,j+l   # 이 로직 ★★★★★★★★★★
                        if not (0 <= dx < len(park) and 0 <= dy < len(park[0])):
                            can_place = False
                            break
                        if park[dx][dy] != "-1" : 
                            can_place = False
                            break
                if can_place :  # 이 로직 ★★★★★★★★★★
                    found = True
                    mats_check[mat_size] = True
            
    if any(mats_check) : 
        answer = max([index for index,val in enumerate(mats_check) if val ])  # 이 로직 ★★★★★★★★★★
    else : 
        answer = -1
    return answer
    
print(solution([5,3,2],[["A", "A", "-1", "B", "B", "B", "B", "-1"],
                        ["A", "A", "-1", "B", "B", "B", "B", "-1"],
                        ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
                        ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], 
                        ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"], 
                        ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]))


                        



                        