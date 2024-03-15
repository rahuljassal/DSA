def backtrack(n,i):
    if i>n:
        return
    else:
        backtrack(n,i+1)
        print(i)

backtrack(3,1)