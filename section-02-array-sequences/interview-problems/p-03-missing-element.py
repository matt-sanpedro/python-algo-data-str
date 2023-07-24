'''
PROBLEM STATEMENT:
Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array. 

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

Input:
    
    finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:

    5 is the missing number
'''

# SOLUTION 1: O(n)
def finder(arr1,arr2):
    for elem in arr1:
        if not (elem in arr2):
            # return elem if not found in arr2
            return elem
        else:
            # handle possible duplicates
            arr2.remove(elem)
        
    return

# SOLUTION 2: O(NlogN)
def finder2(arr1,arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2, in zip(arr1,arr2):
        if num1 != num2:
            return num1
    
    return arr1[-1]

# SOLUTION 3: O(n)
import collections
def finder3(arr1,arr2):
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

# SOLUTION 4: XOR method O(n) and constant space complexity
def finder4(arr1,arr2):
    result = 0

    # perform XOR between numbers in the arrays
    for num in arr1+arr2:
        result^=num
        # print(result)

    return result


arr1 = [1,2,3,4,5,6,7]
# arr2 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
print(finder4(arr1,arr2))

arr1 = [5,5,7,7]
arr2 = [5,7,7]
print(finder4(arr1,arr2))

arr1 = [9,8,7,6,5,4,3,2,1]
arr2 = [9,8,7,5,4,3,2,1]
print(finder4(arr1,arr2))
