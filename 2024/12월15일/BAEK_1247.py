for _ in range(3) : 
    n = int(input())
    number = [int(input()) for _ in range(n)]
    if sum(number) == 0 :
        print(0)
    elif sum(number) >0 : 
        print('+')
    else : 
        print('-')