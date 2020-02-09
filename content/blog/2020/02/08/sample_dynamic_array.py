import ctypes


class DynamicArray:
    """A dynamic array class, akin to a simplified Python
    list. """

    def __init__(self):
        """Create an empty array."""
        self._n = 0
        self._capacity = 1  # default capacity
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """Return the number of elements stored in the
        array. """
        return self._n

    def __getitem__(self, k):
        """Return element at index k. """
        if not 0 <= k < self._n:
            raise IndexError("invalid index")

        return self._A[k]

    def append(self, obj):
        """Add an element to the end of the array. If there
        isn't enough capacity, double the size of the
        array. """
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        """Resize internal array to capacity c. """
        B = self._make_array(c)

        for k in range(self._n):
            B[k] = self._A[k]

        self._A = B
        self._capacity = c

    def _make_array(self, c):
        """Return a new array with capacity c. """
        return (c * ctypes.py_object)()


if __name__ == "__main__":
    A = DynamicArray()
    print(len(A))

    A.append("a")
    print(len(A))

    A.append("b")
    print(len(A))

    A.append("c")
    print(len(A))
    print(A._capacity)
