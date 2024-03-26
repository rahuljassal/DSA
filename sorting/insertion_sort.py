# insertion sort 
# key => put the current value at right place
input_arr = [13,46,24,52,20,9,8,9,9,2]
ordered_arr = [1,2,3,4,5]
# def insertion_sort (arr):
#     n = len(arr)
#     for i in range(0,n):
#         j = i
#         while j>0 and arr[j-1]>arr[j]:
#             temp = arr[j-1]
#             arr[j-1] = arr[j]
#             arr[j] = temp
#             j-=1
#     return arr
def insertion_sort(arr):
    for i in range(len(arr)):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            temp = arr[j-1] 
            arr[j-1] = arr[j]
            arr[j] = temp
            j-=1
    return arr
def rec_insertion_sort(arr,n):
    if n<=1:
        return arr
    rec_insertion_sort(arr,n-1)
    i = n-2
    last =arr[n]
    while i>0 and arr[i]>last:
        temp = arr[i+1]
        arr[i+1] = arr[i]
        arr[i] = temp
    arr[i+1] = last
# print(insertion_sort(input_arr))
print(rec_insertion_sort(input_arr,len(input_arr)))


