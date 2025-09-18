def solution(phone_book):
    phone_set = set(phone_book)

    for number in phone_book : 
        for j in range(len(number)) : 
            if number[:j] in phone_set : 
                return False

    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))