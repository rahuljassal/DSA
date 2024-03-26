# bubble sort
# key => put the maximum value at the end by swapping adjacent index
input_arr = [13, 46, 24, 52, 20, 9, 8, 9, 9, 2]
ordered_arr = [1, 2, 3, 4, 5]


def bubble_sort(arr):
    n = len(arr)
    count = 0
    didSwap = 0
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            # print(i,j)
            count += 1
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                didSwap = 1
        # this will improve the TC from O(N2) to O(N) in case of an ordered array
        if didSwap == 0:
            break

    # for i in range(n,0,-1):
    #     for j in range(0,i-1):
    #         count+=1
    #         if arr[j] > arr[j + 1]:
    #             temp = arr[j + 1];
    #             arr[j + 1] = arr[j];
    #             arr[j] = temp;

    return arr, count


def rec_bubble_sort(arr, n):
    if n == 0:
        return arr
    for i in range(0, n-1):
        if arr[i] > arr[i + 1]:
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp
    rec_bubble_sort(arr, n - 1)


# print(bubble_sort(input_arr))
n = len(input_arr) - 1
# print(rec_bubble_sort(input_arr, n))
arr = [64, 34, 25, 12, 22, 11, 90]
rec_bubble_sort(arr, len(arr))
print("Sorted array:", arr)

# print(bubble_sort(ordered_arr))
