def reverseArray(arr) :
    n = len(arr)-1
    for i in range(0,n):
        if i<n:
            temp = arr [i]
            arr[i]=arr[n]
            arr[n]=temp
            n-=1
        else:
            break
    return arr
def swap(i,l):
    if i <=l:
        return arr
    else:
        temp = arr [i]
        arr[i]=arr[l]
        arr[l]=temp
        return swap(i+1,l-1)
def swapOne(i):
    l =len(arr)-i-1
    if i <=len(arr)/2:
        return arr
    else:
        temp = arr [i]
        arr[i]=arr[l]
        arr[l]=temp
        return swapOne(i+1)
def swapArr(i,l):
    if(i<=l):
        return arr
    else:
        temp=arr[i]
        arr[i]=arr[l]
        arr[l]=temp
        return swapArr(i+1,l-1)
def revArr(i):
    l = len(arr)-i-1
    if i<=len(arr)//2:
        return arr
    else:
        temp =arr[i]
        arr[l]=arr[i]
        arr[l]=temp
        return revArr(i+1)
arr = [1,3,4,5]
print(reverseArray(arr))
print(swap(0,len(arr)))
print(swapOne(0))
print(swapArr(0,len(arr)))
print(revArr(0))



