# insertion sort 
# key => put the current value at right place
input_arr = [13,46,24,52,20,9,8,9,9,2]
ordered_arr = [1,2,3,4,5]
def insertion_sort (arr):
    n = len(arr)
    for i in range(0,n):
        j = i
        while j>0 and arr[j-1]>arr[j]:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j-=1
    return arr
print(insertion_sort(input_arr))

