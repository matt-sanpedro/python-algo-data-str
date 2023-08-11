def fact(n):

    # base case must be defined or function will never end
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
    
print(fact(5))