def char_hashing(c,s):
    hash_arr=[0]*26
    ref_point = ord("a")
    for i in s:
        hash_arr[ord(i)-ref_point]+=1
    return hash_arr[ord(c)-ref_point]
c="a"
s="ajndkasndkffadakdkfjn"
print(s.count("a"))
print(char_hashing(c,s))
