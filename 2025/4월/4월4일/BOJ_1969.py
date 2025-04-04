n, m = map(int, input().split())
numbers = [input().strip() for _ in range(n)]  # strip() 추가해서 개행 제거
result = ""
result_num = 0

for i in range(m):
    dna = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for j in range(n):
        dna[numbers[j][i]] += 1
    
    max_key = sorted(dna.items(), key=lambda x: (-x[1], x[0]))[0][0]
    result += max_key
    result_num += n - dna[max_key]

print(result)
print(result_num)
