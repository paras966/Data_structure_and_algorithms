def factorial(n):
    if(n==0):
        return 1
    subpart = factorial(n-1)
    return n*subpart

print(factorial(5))