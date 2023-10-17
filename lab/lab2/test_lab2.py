import unittest
import pqueue
import mheap

def isMaxHeap(l):
    # first, check the root is the max value of the tree
    # have to trim None values from list for max to work
    if max([i for i in l if i is not None]) != l[0]:
        return False
    # iterate over all nodes with children (other than root)
    # +1 at end so loop includes end condition (last parent node)
    for i in range(1, int((len(l) - 1) / 2) + 1):
        # like heapify, but without swapping or recursion
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        largest = i
        if left_index < len(l) and l[left_index] is not None:
            if l[left_index] > l[i]:
                largest = left_index
        if right_index < len(l) and l[right_index] is not None:
            if l[right_index] > l[largest]:
                largest = right_index
        if largest != i:
            return False
    # if non-heap subtree is never found, it's a heap
    return True

class T0_pqueue_insert(unittest.TestCase):
    def test_1_pq_insert(self):
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [5,4,2,1,3])
        print("\n")

class T1_pqueue_peek(unittest.TestCase):
    def test_1_pq_peek(self):
        print("Just return the fist element of the queue.")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.peek(), 3)
        print("\n")

class T2_pqueue_extract_max(unittest.TestCase):
    def test_1_pq_extract_max(self):
        print("extract and return the maximum element of the queue")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.extract_max(), 3)
        print("\n")

class T5_heap_sort(unittest.TestCase):
    def test_heap_sort_1(self):
        print("\n")
        to_sort_list = [10,24,3,57,4,67,37,87,7]
        sorted_list = mheap.heap_sort(to_sort_list)
        self.assertEqual(sorted_list, [3, 4, 7, 10, 24, 37, 57, 67, 87])
        print("\n")

# test case 2 from assignment
class T3_heap_insert(unittest.TestCase):
    def test_heap_insert(self):
        print("\n")
        heap_data = [6,5,3,4,2,1]
        heap = mheap.max_heap(len(heap_data) + 1)
        for data in heap_data:
            heap.insert(data)
        heap.insert(7)
        self.assertEqual(isMaxHeap(heap.heap), True)
        # test insert on full heap
        with self.assertRaises(Exception):
            heap.insert(8)
        print("\n")

# test case 1 from assignment
class T4_heap_build_heap(unittest.TestCase):
    def test_heap_build_heap(self):
        print("\n")
        heap_data = [1,2,3,4,5,6,7,8]
        heap = mheap.max_heap(len(heap_data), heap_data)
        heap.build_heap()
        self.assertEqual(isMaxHeap(heap.heap), True)
        print("\n")

# test case 3 from assignment
class T6_heap_extract_max(unittest.TestCase):
    def test_heap_extract_max(self):
        print("\n")
        empty_heap = mheap.max_heap()
        with self.assertRaises(Exception):
            maximum = empty_heap.extract_max()
        print("\n")
    
class T7_heap_empty_peek(unittest.TestCase):
    def test_heap_empty_peek(self):
        print("\n")
        # test peek on empty heap
        heap = mheap.max_heap()
        with self.assertRaises(Exception):
            heap.peek()
        print("\n")

# test case 4 from assignment
class T8_pqueue_insert_extract(unittest.TestCase):
    def test_pqueue_insert_extract(self):
        print("\n")
        pq = pqueue.pqueue(8)
        queue_data = [1,2,3,4,5,6,7,8]
        for data in queue_data:
            pq.insert(data)
        # assert valid heap after insert
        self.assertEqual(isMaxHeap(pq.pheap.heap), True)
        extracted = pq.extract_max()
        # assert heap still valid
        self.assertEqual(isMaxHeap(pq.pheap.heap), True)
        print("\n")

class T9_heap_ismaxheap_invalid(unittest.TestCase):
    def test_heap_ismaxheap_invalid(self):
        print("\n")
        # randomly generated heap from
        # http://btv.melezinek.cz/binary-heap.html
        heap_data = [17,14,9,11,3,4,2,10]
        heap = mheap.max_heap(len(heap_data), heap_data)
        # heap no longer valid after sort in place
        heap.sort_in_place()
        self.assertEqual(isMaxHeap(heap.heap), False)
        print("\n")


if __name__ == '__main__':
    unittest.main()