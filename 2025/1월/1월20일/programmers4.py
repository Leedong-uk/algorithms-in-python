from collections import Counter

topping = [1, 2, 3, 1, 4]
cnt = 0

bro = Counter(topping) #처음에 동생이 모두 먹는 환경에서 시작
chul = set()

for i in topping :
    bro[i] -=1
    if bro[i] == 0 :
        del bro[i]
    chul.add(i)
    if len(bro) == len(chul) : 
        cnt +=1
        
print(f"최종 cnt: {cnt}")
