class max_heap(object):
    """Binary max-heap

    Supports most standard heap operations (insert, peek, extract_max).
    Can be used for building a priority queue or heapsort. Since Python
    doesn't have built-in arrays, the underlying implementation uses a
    Python list instead. When initialized, max_heap creates a new list of
    fixed size or uses an existing list.

    Attributes
    ----------
    heap : list
        A list of individual numbers which satisfy the max-heap property
        That being, given a tree visualization of the list, the "root" node
        (or first index) contains the maximum value of the list, as well as
        having the property such that each number in the list is the maximum
        value of itself and each of its two children.

    length : int
        Number of non-null elements in the max-heap

    max_size : int
        Total number of possible elements which can be stored in the list

    Methods
    -------
    get_heap():
    Returns the self.heap list, which contains every value in the heap
    insert(data):
    Adds a new data point to the heap, then traverses the heap bottom-up
    from where the node was added, swapping heap data until the max-heap
    property is satisfied again
    peek():
    Returns the maximum value of the heap, which in a max-heap is the root
    extract_max():
    Removes and returns the maximum value of the heap, traversing the entire
    list and swapping to ensure the max-heap property is still satisfied after
    removal
    sort_in_place():
    Invalidates the max-heap property by sorting the self.heap list in ascending
    order, using the heapsort algorithm
    build_heap():
    Iterates over every child-possessing node in the heap, repeatedly making calls
    to a recursive "heapify" method to construct a max-heap satisfying list from
    the data contained in self.heap"""

    def __init__(self, size = 20, data = None):
        """Initialize a binary max-heap.

        size: Total capacity of the heap.
        data: List containing the desired heap contents. 
              The list is used in-place, not copied, so its contents 
              will be modified by heap operations -- using __swap method.
              If data is specified, then the size field is ignored."""

        # Add to this constructor as needed
        if data is not None:
            self.max_size = len(data)
            self.length = len(data)
            self.heap = data
        else:
            self.max_size = size
            self.length = 0
            self.heap = [None] * size
        
    def get_heap(self):
        try:
            if self.length == 0:
                raise KeyError
        except KeyError:
            print("Error: Tried to get heap, but heap was empty!")
            raise KeyError
        else:
            return self.heap


    def insert(self, data):
        """Insert an element into the heap.

        Raises IndexError if the heap is full."""
        # Tips : insert 'data' at the end of the list initially
        #      : swap with its parent until the parent is larger or you 
        #      : reach the root
        
        try:
            if self.length >= self.max_size:
                raise IndexError
        except IndexError:
            print("Error: Tried to insert to the heap, but the heap was full!")
            raise IndexError
        else:
            # self.length (pre-increment) will refer to the last index in heap
            self.heap[self.length] = data
            # heap should still work if null key is passed in
            if data is None:
                return
            self.length += 1
            curr_index = self.length - 1
            while curr_index > 0:
                parent_index = self.__get_parent(curr_index)
                if self.heap[parent_index] > self.heap[curr_index]:
                    return
                else:
                    self.__swap(parent_index, curr_index)
                    curr_index = parent_index
        
    def peek(self):
        """Return the maximum value in the heap."""
        return self.heap[0]

    def extract_max(self):
        """Remove and return the maximum value in the heap.

        Raises KeyError if the heap is empty."""
        # Tips: Maximum element is first element of the list
        #     : swap first element with the last element of the list.
        #     : Remove that last element from the list and return it.
        #     : call __heapify to fix the heap
        
        try:
            if self.length == 0:
                raise KeyError
        except KeyError:
            print("Tried to extract max from heap, but the heap was empty!")
            raise KeyError
        else:
            self.__swap(0, self.length - 1)
            extracted_max = self.heap.pop(self.length - 1)
            self.heap.append(None)
            self.length -= 1
            self.__heapify(0, self.length)
            return extracted_max

    def sort_in_place(self):
        """Perform heatsort in-place (e.g., reorder elements in ascending order for self.heap)
        Note that the heap is no longer "valid" once this method is called.
        Tip 1. Use the list_length parameter for __heapify method to limit the scope of self.heap
        Tip 2. Only use build_heap once, and then call __heapify for index where max-heap property is violated
        """
        self.build_heap()
        for i in range(self.length - 1, 0, -1):
            self.__swap(0, i)
            self.__heapify(0, i)


    def __heapify(self, curr_index, list_length = None):
        """Recursively moves elements down in the heap
           to satisfy max-heap property of children being
           smaller than the parent"""
        # helper function for moving elements down in the heap
        # Page 157 of CLRS book
        left_index = self.__get_left(curr_index)
        right_index = self.__get_right(curr_index)
        # default value
        largest = curr_index
        if left_index < list_length and self.heap[left_index] > self.heap[curr_index]:
            largest = left_index
        if right_index < list_length and self.heap[right_index] > self.heap[largest]:
            largest = right_index
        if largest != curr_index:
            self.__swap(curr_index, largest)
            self.__heapify(largest, list_length)

    def build_heap(self):
        """Iterates over every child-possessing node in the heap,
           calling recursive heapify method to conduct swaps until
           max-heap property is satisfied for tree and all subtrees
           in list self.heap"""
        # builds max heap from the list l.
        # Tip: call __heapify() to build to the list
        #    : Page 157 of CLRS book
        for i in range(int((self.length - 1) / 2), -1, -1):
            self.__heapify(i, self.length)

    ''' Optional helper methods may be used if required '''
    ''' You may create your own helper methods as required.'''
    ''' But do not modify the function definitions of any of the above methods'''

    def __get_parent(self, loc):
        # left child has odd location index
        # right child has even location index
        # if loc % 2 == 0:
        #     parent = int((loc - 2) / 2)
        # else:
        parent = int((loc - 1) / 2)
        return parent

    def __get_left(self, loc):
        return 2*loc + 1

    def __get_right(self, loc):
        return 2*loc + 2
        

    def __swap(self, a, b):
        # swap elements located at indexes a and b of the heap
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp

def heap_sort(l):
    """The public heap_sort should do the following.
    1. Create a max_heap object using the provided list l
    2. Call sort_in_place method to sort the list "in-place"
    """
    to_sort = max_heap(len(l), l)
    to_sort.sort_in_place()
    return to_sort.heap