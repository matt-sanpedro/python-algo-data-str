def fact(n):
    print('n is: {}'.format(n))

    # base case must be defined or function will never end
    if n == 0:
        return 1
    else:
        print('Computing: {}'.format(n * fact(n - 1)))
        return n * fact(n - 1)
    
print(fact(5))