import unittest
import pqueue
import mheap

class T0_pqueue_insert(unittest.TestCase):
    def test_1_pq_insert(self):
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        print(pq.pheap.heap)
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
        # test peek on empty heap
        with self.assertRaises(Exception):
            pq.peek()
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

class T3_heap_insert(unittest.TestCase):
    def test_heap_insert(self):
        print("\n")
        heap_data = [6,5,3,4,2,1]
        heap = mheap.max_heap(len(heap_data) + 1)
        for data in heap_data:
            heap.insert(data)
        heap.insert(7)
        self.assertEqual(heap.heap, [7,5,6,4,2,1,3])
        # test insert on full heap
        with self.assertRaises(Exception):
            heap.insert(8)
        print("\n")

class T4_heap_build_heap(unittest.TestCase):
    def test_heap_build_heap(self):
        print("\n")
        heap_data = [1,2,3,4,5,6,7,8]
        heap = mheap.max_heap(len(heap_data), heap_data)
        heap.build_heap()
        self.assertEqual(heap.heap, [8,5,7,4,1,6,3,2])
        print("\n")

class T6_heap_extract_max(unittest.TestCase):
    def test_heap_extract_max(self):
        print("\n")
        heap = mheap.max_heap()
        with self.assertRaises(Exception):
            maximum = heap.extract_max()
        print("\n")

if __name__ == '__main__':
    unittest.main()