record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
result = []
final_nick = {}

# 로그 처리
for log in record:
    temp = log.split(" ")
    command, user_id = temp[0], temp[1]
    
    if command == "Enter" or command == "Change":
        nickname = temp[2]
        final_nick[user_id] = nickname
        if command == "Enter":
            result.append(f'{user_id}님이 들어왔습니다.')
    elif command == "Leave":
        result.append(f'{user_id}님이 나갔습니다.')

# result에서 user_id를 final_nick[user_id]로 바꾸기
for i in range(len(result)):
    user_id = result[i].split("님")[0]
    result[i] = result[i].replace(user_id, final_nick[user_id])

print(result)
