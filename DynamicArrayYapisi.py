import ctypes # provides low-level arrays

class DynamicArray:
    def __init__(self):
        self._n=0 # count actual elements
        self._capacity = 1 # default array capacity
        self._A = self._make_array(self._capacity) # low-level array

    def __len__(self):
        return self._n
    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError( 'invalid index')
        return self._A[k] # retrieve from array"
    def append(self, obj):
        if (self._n == self._capacity): # not enough room
            self._resize(2 * self._capacity) # so double capacity
        self._A[self._n] = obj
        self._n += 1
    def _resize(self, c): # nonpublic utitity
        B = self._make_array(c) # new (bigger) array
        for k in range(self._n): # for each existing value
            B[k] = self._A[k]
        self._A=B # use the bigger array
        self._capacity = c

    def _make_array(self, c): # nonpublic utitity
        return (c * ctypes.py_object)( ) # see ctypes documentation
    
c= DynamicArray()
for i in range(10):
    c.append("add an item " + str(i))
    print(str(i) + "eklendi, dizi boyutu " + str(c._capacity)) 
