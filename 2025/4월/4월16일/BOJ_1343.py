import re

board = input()  
# "." 기준으로 나누기
parts = re.split(r"(\.+)", board)  

result = []

for part in parts:
    if part[0] == '.':
        result.append(part)
    else:
        n = len(part)
        if n % 2 != 0:
            print(-1)
            exit()
        # 가능한 만큼 AAAA로 먼저 채우고, 남는 2칸은 BB로
        a_count = n // 4
        b_count = (n % 4) // 2
        result.append("AAAA" * a_count + "BB" * b_count)

print(''.join(result))
