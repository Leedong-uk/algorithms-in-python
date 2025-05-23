from collections import defaultdict

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2
result = [0] * len(id_list)


unique_reports = set(report)
reported_count = defaultdict(int)

# 3. 누가 누구를 신고했는지 저장
reporter_map = defaultdict(list)

for r in unique_reports:
    sender, receiver = r.split()
    reporter_map[sender].append(receiver)
    reported_count[receiver] += 1

banned = set(user for user, count in reported_count.items() if count >= k)

for i, user in enumerate(id_list):
    for target in reporter_map[user]:
        if target in banned:
            result[i] += 1

print(result)
