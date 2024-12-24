n = 15
binary_n = format(n,'b')
current_n = n+1
while True : 
    if binary_n.count('1') == format(current_n,'b').count('1') :
        break
    
    current_n = current_n+1

print(current_n)

    
