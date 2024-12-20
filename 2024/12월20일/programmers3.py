s="abaabab"

index = 0
answer = 0
check = [0,0]

for i in range(len(s)) : 
    if index+1 == len(s) or i+1 == len(s) :
        answer +=1
        break
    if s[i] == s[index] : 
        check[0] +=1
    else : 
        check[1] +=1
    
    print('answer = ',answer,'check = ',check)

    if check[0] == check[1] : 
        answer +=1
        check=[0,0]
        index = i+1
        print('ㅡㅡㅡㅡㅡ문자열 같아짐ㅡㅡㅡㅡㅡ')
        print('index = ',index,'answer = ',answer)
        print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')


print(answer)



