def sumRec(n,sum):
    if 1>n:
        return sum
    else:
        sum = sum +n
        return sumRec(n-1,sum)
def sumFuncRec(n):
    if n==0:
        return 0
    else:
        return n+sumFuncRec(n-1)
print(sumRec(5,0))
print(sumFuncRec(5))
