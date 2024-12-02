
import sys

while True : 
    n = sys.stdin.readline().rstrip("\n")

    if not n :
        break

    s_count = 0
    b_count = 0
    n_count = 0
    count = 0

    for i in n : 
        if 97 <= ord(i) <= 122 : 
            s_count+=1
        elif 65 <= ord(i) <= 90 : 
            b_count+=1
        elif i.isdigit() : 
            n_count +=1 
        elif i.isspace(): 
            count +=1


    print(s_count,b_count,n_count,count)

