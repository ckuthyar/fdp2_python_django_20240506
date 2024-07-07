def fact(num1): 
    fact1=1
    for i in range(1,num1+1,1):
        fact1=fact1*i
    return fact1
result=fact(4)
print(result)
