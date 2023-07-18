import sys

# set n -> amount elements in array
n = 10000

data = []

for i in range(n):
    # print(i)

    # number of elements
    a = len(data)

    # actual size in bytes
    b = sys.getsizeof(data)

    # python overallocates memory for arrays, thus bytes may be constant for different lengths
    print('Length: {0:3d}; Size in bytes: {1:4d} '.format(a, b))

    # increase length by one
    data.append(n)

# for classes, can create private functions by beginning function name with underscore
class M(object):
    def public(self):
        print('Use tab to see me')

    def _private(self):
        print("You won't be able to tab to see me")

m = M()
m.public()
m._private()