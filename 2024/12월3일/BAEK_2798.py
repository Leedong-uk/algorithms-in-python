n , m = map(int,input().split())
num = list(map(int,input().split()))
final_diff = m
final_num = 0

for i in range(n-2) :
    for j in range(i+1,n-1) :
        for k in range (j+1,n) :
                new_num = num[i]+num[j]+num[k]
                new_diff = abs(m-new_num)
                if new_num <= m and new_diff <= final_diff : 
                    final_num = new_num
                    final_diff = new_diff

print(final_num)



