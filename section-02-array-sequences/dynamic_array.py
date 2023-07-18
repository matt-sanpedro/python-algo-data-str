import ctypes, sys

class DynamicArray(object):
    
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, k):

        if not 0 <= k < self.n:
            return IndexError('k is out of bounds!')
        
        return self.A[k]

    def append(self, ele):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        
        self.A[self.n] = ele
        self.n += 1

    def _resize(self, new_cap):
        B = self.make_array(new_cap)

        # re-reference the B array with A array contents
        for k in range(self.n):
            B[k] = self.A[k]
        
        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        '''
        makes raw array

        ctypes -> allocating raw bytes to create array
        '''
        return (new_cap * ctypes.py_object)()

# IMPLEMENTATION
arr = DynamicArray()
print(len(arr))
n = 1000000

for i in range(n):
    # print(i)
    arr.append(i)
print('Length: {0:3d}; Size in bytes: {1:4d} '.format(len(arr), sys.getsizeof(arr)))

animalArray = ['cat', 'dog', 'mouse', 'horse', 'parrot', 'bear', 'tiger', 'lion']
print('Size in bytes of array: {}'.format(sys.getsizeof(animalArray)))
