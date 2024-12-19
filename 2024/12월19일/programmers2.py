wallet = [30,15]
bill = [26,17]
answer = 0

while min(bill) > min(wallet) or max(bill) > max(wallet) : 
    if bill[0] > bill[1] : 
        bill[0] = bill[0] //2
    else : 
        bill[1] = bill[1]//2
    
    answer +=1
print(answer)