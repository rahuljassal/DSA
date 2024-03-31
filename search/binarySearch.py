arr = [1, 2, 3, 4, 5, 64, 86, 99]


def binarySearch(arr, n, target):
    low = 0
    high = n - 1
    count = 0
    while low <= high:
        count += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, count
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1, count


def recBinary(arr, n, target):
    def recBinarySearch(arr, low, high):
        mid = (low + high) // 2
        if low > high:
            return -1
        elif arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return recBinarySearch(arr, mid + 1, high)
        else:
            return recBinarySearch(arr, low, mid - 1)

    return recBinarySearch(arr, 0, n - 1)


print(recBinary(arr, len(arr), 86))
