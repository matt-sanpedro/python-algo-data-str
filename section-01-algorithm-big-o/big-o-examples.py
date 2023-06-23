'''
O(1) Constant

Always constant irregardless of list size\
'''
def func_constant(values):
    print(values[0])

lst = [1, 2, 3]
func_constant(lst)

'''
O(n) Linear

Scales linearly with n
'''
def func_lin(lst):
    for val in lst:
        print(val)

func_lin(lst)

'''
O(n^2) Quadratic

For a list of n items, need to perform n operations
A list of 10 items will need 100 operations
'''
def func_quad(lst):
    for item_1 in lst:
        for item_2 in lst:
            print(item_1, item_2)

func_quad(lst)


'''
When it comes to big-o notation, the significant terms matter

Usually, can drop insignificant terms for Big-O analysis
'''
# Big-O of O(n) or linear
def print_once(lst):
    for val in lst:
        print(val)

# Big-O of O(n) or linear (since O(2n) -> O(n) as n approaches infinity)
def print_2(lst):
    for val in lst:
        print(val)
    
    for val in lst:
        print(val)

'''
For the function "comp" perform Big-O Analysis

Adding all three components:
O(1 + n/2 + 10)

As n grows larger, the 1 and 10 constants become insignificant

O(n)
'''
def comp(lst):
    # O(1)
    print(lst[0])

    # O(n/2) ... O(1/2 * n)
    midpoint = len(lst) // 2

    for val in lst[:midpoint]:
        print(val)

    # O(10)
    for x in range(10):
        print('hello world')

lst = list(range(1,11))
print(lst)
comp(lst)

'''
For the matcher function, there are best/worst case scenarios

Best case: O(1) since match is found at first element
Worst case: O(n) if there is no match
'''
def matcher(lst, match):
    for item in lst:
        if item == match:
            return True
    return False

print(matcher(lst, 11))

# create_list function has Big-O time complexity of O(n)
def create_list(n):
    new_list = []

    for num in range(n):
        new_list.append('new')

    return new_list

print(create_list(5))

'''
time complexity: O(n)

space complexity: O(1) is a constant since only need to save "hello world"
'''
def printer(n):
    for x in range(10):
        print('hello world')

print(printer(10))
