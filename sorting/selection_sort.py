arr = [12, 34, 11, 3, 67, 54, 40, 1, 0, 11, 45]
arr1 = [3, 11, 12, 34, 40, 54, 67]
# expected output [3,11,12,34,40,54,67]
# selection sort => select minimum and then swap it with the first


def selection_sort(unsorted_arr):
    for i in range(0, len(unsorted_arr) - 1):
        for j in range(i, len(unsorted_arr)):
            min_num = unsorted_arr[i]
            if min_num > unsorted_arr[j]:
                temp = unsorted_arr[j]
                unsorted_arr[j] = unsorted_arr[i]
                unsorted_arr[i] = temp
    return unsorted_arr