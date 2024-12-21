from collections import Counter
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
hash_dict = {}
sum_hash = 0

dict_result = Counter(participant) - Counter(completion)
answer = list(dict_result.keys())[0]
print(answer)