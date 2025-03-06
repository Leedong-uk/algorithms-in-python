skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
cnt = 0

for skills in skill_trees :
    prior_index = 0 
    for alpha in skills : 
        if alpha in skill : 
            if alpha == skill[prior_index] : 
                prior_index +=1
            else : 
                break
    else : 
        cnt +=1
        
print(cnt)