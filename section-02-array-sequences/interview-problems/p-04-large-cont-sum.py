'''
PROBLEM STATEMENT:
Given an array of integers (positive and negative) find the largest continuous sum. 
'''
# SOLUTION 1: O(n)
def large_cont_sum(arr): 
    # edge case: arr not long enough
    if len(arr) == 0:
        return 0

    # parameters for tracking largeest continuous sum
    large_sum = 0
    # start_index = 0
    # end_index = 0

    # initial parameters
    current_sum = 0

    for index, num in enumerate(arr):
        current_sum += num

        if current_sum > large_sum:
            large_sum = current_sum
            # start_index = index
        if current_sum < 0:
            # start_index = index
            # end_index = index
            current_sum = 0

    print('Largest sum: {}'.format(large_sum))
    # print('Start index: {}'.format(start_index))
    # print('End index: {}'.format(end_index))

large_cont_sum([1,2,-1,3,4,10,10,-10,-1]) # 29
large_cont_sum([1,2,-1,3,4,-1])
large_cont_sum([-1,1])
