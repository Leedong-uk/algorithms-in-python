n, k = map(int, input().split())
data = []

# 입력 데이터를 받으며 국가 번호를 포함시킴
for i in range(n):
    order, gold, silver, bronze = map(int, input().split())
    data.append((order, gold, silver, bronze))

# 메달 순위로 정렬 (금 -> 은 -> 동), 동점 처리하기 위해 음수로 정렬
data.sort(key=lambda x: (-x[1], -x[2], -x[3]))

# 순위 계산
rank = 1
ranks = [0] * (n + 1)  # 각 국가의 순위를 저장할 리스트
for i in range(n):
    # 이전 국가와 메달 개수가 같다면 같은 순위 부여
    if i > 0 and data[i][1:] == data[i - 1][1:]:
        ranks[data[i][0]] = rank
    else:
        rank = i + 1
        ranks[data[i][0]] = rank

# k번 국가의 순위 출력
print(ranks[k])
