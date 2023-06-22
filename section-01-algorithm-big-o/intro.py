import time

def sum1(n):
    # iteratively adds the numbers
    final_sum = 0
    for x in range(n+1):
        print('x is: {}'.format(x))
        final_sum += x

    print('Final sum is: {}'.format(final_sum))
    return final_sum

start_time = time.time()
sum1(5)
# 0.001997709274291992 seconds
print("--- %s seconds ---" % (time.time() - start_time))

def sum2(n):
    final_sum = (n*(n+1))/2
    print('Final sum is: {}'.format(final_sum))
    return final_sum

start_time = time.time()
sum2(5)
# 0.0 seconds
print("--- %s seconds ---" % (time.time() - start_time))
