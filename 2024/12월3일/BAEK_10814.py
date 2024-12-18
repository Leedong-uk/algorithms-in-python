n = int(input())
account = []

for i in range(n) :
    age , name  = input().split()
    account.append((int(age),name,i))

account.sort(key = lambda x : (x[0],x[2]))

for i in range(n) : 
    print(account[i][0],account[i][1])

