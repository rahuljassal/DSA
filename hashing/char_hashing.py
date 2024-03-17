from collections import defaultdict
def char_hashing(c,s):
    hash_arr=[0]*26
    ref_point = ord("a")
    for i in s:
        hash_arr[ord(i)-ref_point]+=1
    return hash_arr[ord(c)-ref_point]
c="a"
s="ajndkasndkffadakdkfjn"
def map_char_hashing(c,s):
    hash_dict = {}
    for i in s:
        if hash_dict.get(i):
            hash_dict[i]=hash_dict[i]+1  
        else:
            hash_dict[i]=1
    for x in hash_dict:
        print(x,"=>",hash_dict[x])
    return hash_dict.get(c)

def unordered_map_char_hashing(c,s):
    hash_dict = defaultdict(int)
    for i in s:
        hash_dict[i]=hash_dict[i]+1 
    return hash_dict.get(c)

print(s.count("a"))
print(char_hashing(c,s))
print(map_char_hashing(c,s))
print(unordered_map_char_hashing(c,s))


