count = 0
def recursion(count):
    count+=1
    if count<5:
        print("hello",count)
        recursion(count)
    else:
        return

recursion(count)