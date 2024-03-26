# def merge_rec(arr, low, high):
#     if low >= high:
#         return
#     mid = (low + high) // 2
#     merge_rec(arr, low, mid)
#     merge_rec(arr, mid + 1, high)
#     return merge(arr, low, mid, high)


# def merge(arr, low, mid, high):
#     temp = []
#     left = low
#     right = mid + 1
#     while left <= mid and right <= high:
#         if arr[left] <= arr[right]:
#             temp.append(arr[left])
#             left += 1
#         else:
#             temp.append(arr[right])
#             right += 1
#     while left <= mid:
#         temp.append(arr[left])
#         left += 1
#     while right <= high:
#         temp.append(arr[right])
#         right += 1
#     for i in range(low,high+1):
#         arr[i]=temp[i-low]
#     return arr
def merge_rec(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_rec(arr, low, mid)
    merge_rec(arr, mid + 1, high)
    return merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right +=1
    for i in range(low,high+1):
        arr[i]= temp[i-low]
    return arr




arr = [3, 1, 2, 4, 1, 5, 6, 2, 4]
print(merge_rec(arr, 0, len(arr) - 1))
