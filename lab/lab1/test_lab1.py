import lab1
import unittest

class T0_TestingQueue(unittest.TestCase):

    def test_basic_enqueue(self):
        # testing the basic enqueue operation
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)

        self.assertEqual(q.__str__(), '[1, 2, 3, 4]')
        print("\n")
    
    def test_basic_dequeue(self):
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)
        self.assertEqual(1, q.dequeue())
        # test dequeue of empty queue
        with self.assertRaises(Exception):
            q.dequeue()
        print("\n")

class T1_TestingStack(unittest.TestCase):

    def test_is_empty_false(self):
        # testing if stack is empty
        print("\n")
        s = lab1.Stack()
        s.push("4")
        print("return false if the stack is not empty")
        self.assertEqual(s.isEmpty(), False)
        print("\n")
    
    def test_basic_push(self):
        # testing the basic push operation
        print("\n")
        s = lab1.Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        
        self.assertEqual(s.__str__(), "[4, 3, 2, 1]")
        print("\n")

    def test_basic_pop(self):
        print("\n")
        s = lab1.Stack()
        s.push(1)
        self.assertEqual(1, s.pop())
        with self.assertRaises(Exception):
            s.pop()
        print("\n")

class T2_TestingPalindrome(unittest.TestCase):

    def test_basic_string(self):
        # testing with basic string
        print("\n")
        string = "hello"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, False)
        print("\n")

    def test_tacocat_string(self):
        print("\n")
        string = "TaCo CaT"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, True)
        print("\n")

if __name__ == '__main__':
    unittest.main()
