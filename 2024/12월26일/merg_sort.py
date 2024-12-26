# 재귀를 이용한 합병 정렬 함수 정의
def merge_sort(arr):
    # 종료 조건은 배열의 길이가 0 또는 1일 때
    if len(arr) <= 1:
        return arr

    # 절반으로 나누어 왼쪽 배열과 오른쪽 배열로 분할
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 아까 나눈 왼쪽 배열과 오른쪽 배열을 각각 다시 호출
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # 왼쪽 배열과 오른쪽 배열을 합병한 것을 반환
    return merge(left_half, right_half)

# 합병 함수 정의
def merge(left_half, right_half):
    # 반환할 배열과 왼쪽 절반과 오른쪽 절반에 대한 인덱스 초기화
    result = []
    i = j = 0

    # 왼쪽 절반이나 오른쪽 절반 중 인덱스가 초과할 때까지 반복
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1

    # 위의 루프에서 초과했을 경우 남은 부분 배열을 모두 더함
    result += left_half[i:]
    result += right_half[j:]

    # 정렬된 배열 반환
    return result


# 테스트 코드
if __name__ == "__main__":
    array = [6, 5, 3, 1, 8, 7, 2, 4]
    print(array)
    print(merge_sort(array))