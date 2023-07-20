'''
Array Pair Problem Statement:
Given an integer array, output all the ** *unique* ** pairs that sum up to a specific value **k**.

So the input:
    
    pair_sum([1,3,2,2],4)

would return **2** pairs:

     (1,3)
     (2,2)

**NOTE: FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS**
'''
# SOLUTION 1: Brute force method [O(n^2)]
def pair_sum(arr,k):
    unique_list = []
    count = 0

    for i in range(len(arr)):
        # print(i)
        for j in range(len(arr)):
            # cannot use a number twice in addition, so skip if the index is the same
            if i == j:
                continue
            
            # check if array sum is equal to k
            if (arr[i]+arr[j]) == k:
                print(arr[i],arr[j])

                # check if pair already exists in unique_list array of sets
                # skip pair with "continue"
                if (arr[i],arr[j]) in unique_list or (arr[j],arr[i]) in unique_list:
                    continue

                if arr[i] < arr[j]:
                    unique_list.append((arr[i], arr[j]))
                else:
                    # either (arr[j] > arr[i]) or (arr[j] = arr[i])
                    unique_list.append((arr[j], arr[i]))

            # print(unique_list)
    
    print('Unique list: {}'.format(unique_list))
    return len(unique_list)

# print(pair_sum([1,3,2,2],4))
# print(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))

# SOLUTION 2: Linear scan of array with sets [O(n)]
def pair_sum2(arr,k):
    # Edge case check: return None if length of arr less than 2
    if len(arr) < 2:
        return
    
    # sets for tracking: converting O(n^2) and reduce to linear O(n)
    seen = set()
    output = set()

    '''
    ([1,3,2,2],4)

    Initialized:
    seen = {}
    output = {}

    num = 1:
    seen = {1}
    output = {}

    num = 3:
    seen = {1}
    output = {(1,3)}

    num = 2:
    seen = {1,2}
    output = {(1,3)}

    num = 2:
    seen = {1,2}
    output = {(1,3), (2,2)}
    '''
    for num in arr:
        # print('ON num: {}'.format(num))
        target = k - num

        if target not in seen:
            # print('Adding to seen: {}'.format(num))
            seen.add(num)
        else:
            pair = (min(num,target), max(num,target))
            # print('Adding to output: {}'.format(pair))
            output.add(pair)
    
    print(output)
    return len(output)

print(pair_sum2([1,3,2,2],4))
