import unittest
import pqueue
import mheap

"""All 'correct' heaps used in equal assertions were retrieved from
   http://btv.melezinek.cz/binary-heap.html"""

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
        self.assertEqual(heap.get_heap(), [7,5,6,4,2,1,3])
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
        self.assertEqual(heap.get_heap(), [8,5,7,4,1,6,3,2])
        print("\n")

# test case 3 from assignment
class T6_heap_extract_max(unittest.TestCase):
    def test_heap_extract_max(self):
        print("\n")
        # test extract_max from empty heap
        # extract_max itself tested in T2
        empty_heap = mheap.max_heap()
        with self.assertRaises(Exception):
            maximum = empty_heap.extract_max()
        print("\n")
    
class T7_heap_empty_peek(unittest.TestCase):
    def test_heap_empty_peek(self):
        print("\n")
        # test peek on empty heap
        heap = mheap.max_heap()
        self.assertEqual(None, heap.peek())
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
        self.assertEqual(pq.get_pqueue(), [8,7,6,4,3,2,5,1])
        pq.extract_max()
        # assert heap still valid
        self.assertEqual(pq.get_pqueue(), [7,4,6,1,3,2,5,None])
        print("\n")

class T9_heap_get_heap(unittest.TestCase):
    def test_heap_get_heap(self):
        print("\n")
        empty_heap = mheap.max_heap()
        with self.assertRaises(Exception):
            empty_heap.get_heap()
        print("\n")

class T10_pqueue_is_empty(unittest.TestCase):
    def test_pqueue_is_empty(self):
        print("\n")
        pq = pqueue.pqueue(5)
        self.assertEqual(pq.is_empty(), True)
        pq.insert(1)
        self.assertEqual(pq.is_empty(), False)
        print("\n")

class T11_heap_peek_is_max(unittest.TestCase):
    def test_heap_peek_is_max(self):
        print("\n")
        heap_data = [10,8,5,7,0,4,2,3,1]
        heap = mheap.max_heap(None, heap_data)
        self.assertEqual(max(heap_data), heap.peek())
        print("\n")

class T12_heap_insert_null(unittest.TestCase):
    def test_heap_insert_null(self):
        print("\n")
        heap_data = [10,8,5,7,0,4,2,3,1]
        heap = mheap.max_heap(None, heap_data)
        heap.extract_max()
        heap.insert(None)
        self.assertEqual(heap.get_heap(), [8,7,5,3,0,4,2,1,None])
        self.assertEqual(len([i for i in heap.get_heap() if i is not None]), heap.length)
        print("\n")

class T13_heap_test_multiple_extractmax(unittest.TestCase):
    def test_heap_multiple_extractmax(self):
        print("\n")
        heap_data = [10,8,5,7,0,4,2,3,1]
        heap = mheap.max_heap(None, heap_data)
        max1 = heap.extract_max()
        max2 = heap.extract_max()
        max3 = heap.extract_max()
        self.assertEqual(max1, 10)
        self.assertEqual(max2, 8)
        self.assertEqual(max3, 7)
        print("\n")

class T14_heap_unheap_reheap(unittest.TestCase):
    def test_heap_unheap_reheap(self):
        print("\n")
        to_sort_list = [10,24,3,57,4,67,37,87,7]
        heap = mheap.max_heap(len(to_sort_list), to_sort_list)
        heap.sort_in_place()
        self.assertEqual(heap.get_heap(), [3, 4, 7, 10, 24, 37, 57, 67, 87])
        heap.build_heap()
        self.assertEqual(heap.get_heap(), [87,67,57,10,24,37,7,4,3])
        print("\n")

if __name__ == '__main__':
    unittest.main()