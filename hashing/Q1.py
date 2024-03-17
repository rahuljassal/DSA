# Example 1:
# Input: 
arr = [10,5,10,15,10,5]
# Output: 10  3
# 	       5  2
#         15  1
# Explanation: 10 occurs 3 times in the array
# 	      5 occurs 2 times in the array
#               15 occurs 1 time in the array
from collections import defaultdict

def countOccurence(arr):
    # TC O(logN) if ordered O(1) if onordered
    # SC O(N) 

    hash_dict = defaultdict(int)
    for i in arr:
        hash_dict[i]+=1
    # for x in hash_dict:
    #     print(f"{x} {hash_dict[x]}")
    return hash_dict
# print(countOccurence(arr))

# Example 1:
# Input: array[] = {10,5,10,15,10,5};
# Output: 10 15
# Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.
def maxMin(arr):
    new_obj = countOccurence(arr)
    print(new_obj)
    max_k, max_v = max(new_obj.items(), key=lambda x: x[1])
    min_k, min_v = min(new_obj.items(), key=lambda x: x[1])
    return min_k,max_k

print(maxMin(arr))


