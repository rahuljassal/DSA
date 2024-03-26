def quick_sort(arr, low, high):
    if low < high:
        partition = get_partition(arr, low, high)
        print(partition)
        quick_sort(arr, low, partition - 1)
        quick_sort(arr, partition + 1, high)
        return arr


def get_partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        while arr[j] > pivot and j >= low + 1:
            j -= 1
        if i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[low]
    arr[low] = arr[j]
    arr[j] = temp
    return j


arr = [3, 1, 2, 4, 1, 5, 6, 2, 4]
# print(arr)
quick_sort(arr, 0, len(arr) - 1)
print(arr)


def quick_sort_v1(arr, low, high):
    if low < high:
        partition = get_partition_v1(arr, low, high)
        quick_sort_v1(arr, low, partition - 1)
        quick_sort_v1(arr, partition + 1, high)
        return arr


def get_partition_v1(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] >= pivot and i <= high-1:
            i += 1
        while arr[j] <= pivot and j >= low+1:
            j -= 1
        if i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[low]
    arr[low] =arr[j]
    arr[j] =temp
    return j
quick_sort_v1(arr, 0, len(arr) - 1)
print(arr)