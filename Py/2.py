def getFact(n):
    fact1=1
    for i in range(1,n+1,1):
        fact1=fact1*i
    return fact1
print(getFact(5))
print(getFact(6))
