import lab3
import unittest



class T0_tree__insert(unittest.TestCase):

    def test_balanced_binary_search_tree(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        #The following check is without using tree as an iterator (which uses inorder traversal)
        #So this function also does not check the implementation of the traversal function

        self.assertEqual(t.root.data, 4)
        self.assertEqual(t.root.left.data, 2)
        self.assertEqual(t.root.left.left.data, 1)
        self.assertEqual(t.root.left.right.data, 3)
        self.assertEqual(t.root.right.data, 6)
        self.assertEqual(t.root.right.left.data, 5)
        self.assertEqual(t.root.right.right.data, 7)

        print("\n")


class T1_min_and_max(unittest.TestCase):

    def test_min_and_max(self):
        print("\n")
        print("Checkin the min and the max functions")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        minimum = t.min()
        self.assertEqual(minimum, 1)
        maximum = t.max()
        self.assertEqual(maximum, 7)

        print("\n")

class T2_Traversal(unittest.TestCase):

    def test_traversal(self):
        print("\n")
        print("Checking all the three traversals")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)
        tree_iterator = [node for node in t]
        inorder = [node for node in t.inorder()]
        preorder = [node for node in t.preorder()]
        

        print("__iter__(): inorder traversal")
        self.assertEqual(tree_iterator, [1, 2, 3, 4, 5, 6, 7])
        print("inorder traversal")
        self.assertEqual(inorder, [1, 2, 3, 4, 5, 6, 7])
        print("preorder traversal")
        self.assertEqual(preorder, [4, 2, 1, 3, 6, 5, 7])
        print("\n")




class T3_successor(unittest.TestCase):

    def test_successor(self):
        print("\n")
        print("successor function")
        tree_success = lab3.Tree()
        tree_success.insert(8)
        tree_success.insert(3)
        tree_success.insert(10)
        tree_success.insert(1)
        tree_success.insert(6)
        tree_success.insert(4)
        tree_success.insert(7)
        tree_success.insert(14)
        tree_success.insert(13)

        easy_success = tree_success.find_successor(8).data
        medium_success = tree_success.find_successor(10).data
        tough_success = tree_success.find_successor(7).data

        self.assertEqual(easy_success, 10)
        self.assertEqual(medium_success, 13)
        self.assertEqual(tough_success, 8)

        print("\n")


class T4_delete(unittest.TestCase):

    def test_delete(self):
        print("\n")
        print("delete function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)

        l1 = [node for node in t]
        t.delete(7)
        l2 = [node for node in t]
        t.delete(6)
        l3 = [node for node in t]
        t.delete(8)
        l4 = [node for node in t]
        t.delete(10)
        l5 = [node for node in t]



        self.assertEqual(l1, [1, 3, 4, 6, 7, 8, 10, 13, 14])
        self.assertEqual(l2, [1, 3, 4, 6, 8, 10, 13, 14])
        self.assertEqual(l3, [1, 3, 4, 8, 10, 13, 14])
        self.assertEqual(l4, [1, 3, 4, 10, 13, 14])
        self.assertEqual(l5, [1, 3, 4, 13, 14])

        print("\n")

class T5_contains(unittest.TestCase):

    def test_contains(self):
        print("\n")
        print("contains function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)
        self.assertEqual(t.contains(13), True)
        self.assertEqual(t.contains(15), False)
        print("\n")

class T6_my_tree_insert(unittest.TestCase):
    def test_my_tree_insert(self):
        print("\n")
        print("Testing tree insert, manual preorder traverse")
        t = lab3.Tree()
        tree_nodes = [5, 4, 8, 7, 11, 10, 12]

        for node in tree_nodes:
            t.insert(node)
        
        self.assertEqual(t.root.data, 5)
        self.assertEqual(t.root.left.data, 4)
        self.assertEqual(t.root.right.data, 8)
        self.assertEqual(t.root.right.left.data, 7)
        self.assertEqual(t.root.right.right.data, 11)
        self.assertEqual(t.root.right.right.left.data, 10)
        self.assertEqual(t.root.right.right.right.data, 12)

        print("\n")

class T7_my_tree_traverse(unittest.TestCase):
    def test_traverse(self):
        print("\n")
        print("Testing tree traversals")
        t = lab3.Tree()
        tree_nodes = [5, 4, 8, 7, 11, 10, 12]

        for node in tree_nodes:
            t.insert(node)
        
        inorder = [node for node in t.inorder()]
        preorder = [node for node in t.preorder()]
        postorder = [node for node in t.postorder()]

        print("testing inorder traversal")
        self.assertEqual(inorder, [4, 5, 7, 8, 10, 11, 12])
        print("testing preorder traversal")
        self.assertEqual(preorder, [5, 4, 8, 7, 11, 10, 12])
        print("testing postorder traversal")
        self.assertEqual(postorder, [4, 7, 10, 12, 11, 8, 5])

        print("\n")

class T8_my_tree_find_node(unittest.TestCase):
    def test_tree_find_node(self):
        print("\n")
        print("Testing 'find node in tree' helper method")
        t = lab3.Tree()
        tree_nodes = [5, 4, 8, 7, 11, 10, 12]
        for node in tree_nodes:
            t.insert(node)

        # call 'private' method like this, because python
        found = t._Tree__find_node(10)
        self.assertEqual(found, t.root.right.right.left)

        print("Testing return type when node not found")
        found = t._Tree__find_node(14)
        self.assertEqual(found, None)

        print("\n")

class T9_my_tree_contains(unittest.TestCase):
    def test_tree_contains(self):
        print("\n")
        print("Testing tree contains method")
        t = lab3.Tree()
        tree_nodes = [5, 4, 8, 7, 11, 10, 12]
        for node in tree_nodes:
            t.insert(node)
        
        print("Testing node in tree")
        self.assertEqual(t.contains(12), True)
        print("Testing node not in tree")
        self.assertEqual(t.contains(14), False)

        print("\n")

class T10_my_tree_find_successor(unittest.TestCase):
    def test_tree_find_succ(self):
        print("\n")
        print("Testing tree 'find successor' method")
        t = lab3.Tree()
        tree_nodes = [17, 12, 9, 5, 6, 14, 20, 19]
        for node in tree_nodes:
            t.insert(node)

        successor_1 = t.find_successor(12).data
        successor_2 = t.find_successor(5).data
        successor_3 = t.find_successor(17).data

        self.assertEqual(successor_1, 14)
        self.assertEqual(successor_2, 6)
        self.assertEqual(successor_3, 19)

        print("Testing successor of node not in tree")
        with self.assertRaises(Exception):
            successor_trap = t.find_successor(18)

        print("\n")

class T11_my_tree_delete(unittest.TestCase):
    def test_tree_delete(self):
        print("\n")
        print("Testing tree delete function")
        print("NOTE: This test case requires working iterator")
        t = lab3.Tree()
        tree_nodes = [17, 12, 9, 5, 6, 14, 20, 19]
        for node in tree_nodes:
            t.insert(node)

        no_del = [node for node in t]
        t.delete(6)
        first_del = [node for node in t]
        t.delete(9)
        second_del = [node for node in t]
        t.delete(17)
        third_del = [node for node in t]

        self.assertEqual(no_del, [5, 6, 9, 12, 14, 17, 19, 20])
        self.assertEqual(first_del, [5, 9, 12, 14, 17, 19, 20])
        self.assertEqual(second_del, [5, 12, 14, 17, 19, 20])
        self.assertEqual(third_del, [5, 12, 14, 19, 20])

        print("Testing delete of node not in tree")
        with self.assertRaises(Exception):
            t.delete(18)
        print("\n")

if __name__ == '__main__' :
    unittest.main()