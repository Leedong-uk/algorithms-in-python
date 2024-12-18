def merge_sort (arr,low,high) :
    if low >= high : 
        return
    mid = (low + high) //2 

    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    result = merge(arr,low,mid,high)

    return result


def merge (arr,low,mid,high) : 
    temp = []
    i , j = low , mid+1  #각 배열의 시작점 

    while i <= mid and j <= high:
        if arr[i] <= arr[j] : 
            temp.append(arr[i])
            i += 1
        else : 
            temp.append(arr[j])
            j += 1 
    
    while i <= mid : 
        temp.append(arr[i])
        i +=1
    
    while j <= high : 
        temp.append(arr[j])
        j +=1
    

    for k in range (low,high+1) : 
        arr[k] = temp[k-low]
    

    return arr


if __name__ == "__main__":
    n = int(input())
    num = [int(input()) for _ in range(n)]
    
    merge_sort(num, 0, n - 1)
    
    for x in num : 
        print(x)
