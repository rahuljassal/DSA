def find_occurence(n,arr):
    count =0
    for i in arr:
        if i ==n:
            count= count+1
    return count

def find_occurence_hashing():
    n = int(input("size of array "))
    arr = []
    for i in range(0,n):
        inp = int(input(f"add arr[{i}] "))
        arr.append(inp)
    hash1 =[]
    s = int(input("range of numbers"))
    value = int(input("value you want to find"))
    for j in range(0,s):
        hash1.append(0)
    # precomputation
    for i in range(0,n):
        hash1[arr[i]]+=1
    return hash1[value]

# print(find_occurence(n,arr))
print(find_occurence_hashing())