def solution(clothes):
    clothes_dic = {}
    
    # 의상 종류별로 개수를 세기
    for val, key in clothes:
        if key not in clothes_dic:
            clothes_dic[key] = 0
        clothes_dic[key] += 1
    
    # 모든 종류의 선택지를 곱하고 아무것도 입지 않는 경우 제외
    result = 1
    for count in clothes_dic.values():
        result *= (count + 1)  # 각 종류에서 선택하지 않는 경우 포함
    
    return result - 1  # 아무것도 입지 않는 경우 제외