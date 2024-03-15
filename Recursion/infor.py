def get_common_gbu(arr1,arr2):
            a_set = set(arr1)
            b_set = set(arr2)

            if a_set & b_set:
                return True
            else:
                return False
a=["Hygiene"]
b=["Health"]
print(get_common_gbu(b,a))