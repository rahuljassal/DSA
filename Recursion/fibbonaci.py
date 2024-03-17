def nth_fibbonaci(n):
    if n<=1:
        return n
    return nth_fibbonaci(n-1)+ nth_fibbonaci(n-2)
print(nth_fibbonaci(7))