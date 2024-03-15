def fact(n):
    factSum = 1
    for i in range(1,n+1):
        factSum = factSum * i
    return factSum
def recFact(n):
    if n==1:
        return 1
    else:
        return recFact(n-1)*n
print(fact(5))
print(recFact(5))