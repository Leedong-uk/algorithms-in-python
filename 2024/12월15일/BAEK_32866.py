origin = int(input())
x = int(input())
after = origin*((100-x)/100)
result = (origin/after*100)-100
print('{:.6f}'.format(result))
