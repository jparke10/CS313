class Node(object):
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data

class Tree(object):
    """Binary search tree

    Conforms to a standard binary search tree data structure, such that
    the key of each internal node is greater than all the keys in the respective
    node's left subree and less than all the keys in the respective node's
    right subtree. Uses a triply-linked list implementation with standard Node
    objects and supports methods such as insert, delete, search, and successor.

    Attributes
    ----------
    root : Node
        The root of the tree, which is defined as None in the default constructor
        but is filled in with a Node object by tree operations. Root node contains
        pointers to the node(s) throughout the rest of the tree

    Methods
    -------
    print():
        Prints the data of all tree nodes, in order (sorted)
    insert(data):
        Constructs a new node with the input data and adds it to the tree in the
        correct spot
    min():
        Returns the minimum value of any node in the tree
    max():
        Returns the MAXIMUM value of any node in the tree
    __find_node(data):
        Searches for the node with the given data and returns it. If it is not
        in the tree, returns None
    contains(data):
        Uses __find_node method to return a Boolean value stating whether or not
        the input node is in the tree
    __traverse(curr_node, traversal_type):
        Recursively yields each node of the tree depending on standard tree traversal
        types (in-order, pre-order, post-order), allowing for iteration over the tree
    find_successor(data):
        Finds the next largest node in the tree (aka, the smallest key greater than
        the input key) and returns it.
    delete(data):
        Locate the node corresponding to the input data and remove it from the tree,
        replacing it with its successor if it had two children (otherwise shifting its
        children to the correct new position)
    """

    # Binary Search Tree
    # class constants
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    def __init__(self):
        # Do not create any other private variables.
        # You may create more helper methods as needed.
        self.root = None

    def print(self):
        # Print the data of all nodes in order
        self.__print(self.root)


    def __print(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        if curr_node is not None:
            self.__print(curr_node.left)
            print(str(curr_node.data), end=' ')  # save space
            self.__print(curr_node.right)
            

    def insert(self, data):
        # Find the right spot in the tree for the new node
        # Make sure to check if anything is in the tree
        # Hint: if a node n is None, calling n.data will cause an error
        node = Node(data)
        # y represents the destination parent of the new node
        # x is a helper "pointer" used to locate the correct parent
        # of the new node
        y = None
        x = self.root
        while x is not None:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right
        node.parent = y
        # if node's parent is None, it's the new root
        if y is None:
            self.root = node
        # else, insert node depending on inequality relative to parent
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

    def min(self):
        # Returns the minimum value held in the tree
        # Returns None if the tree is empty
        if self.root is None:
            return None
        # Minimum is the leftmost node in the tree
        minimum = self.root
        while minimum.left is not None:
            minimum = minimum.left
        return minimum.data

    def max(self):
        # Returns the maximum value held in the tree
        # Returns None if the tree is empty
        if self.root is None:
            return None
        # Conversely, maximum is rightmost node in the tree
        maximum = self.root
        while maximum.right is not None:
            maximum = maximum.right
        return maximum.data

    def __find_node(self, data):
        # returns the node with that particular data value else returns None
        curr = self.root
        # Iterate over tree, comparing equality to the data of the current node
        # until we hit the correct node
        while curr is not None and data != curr.data:
            if data < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def contains(self, data):
        # return True of node containing data is present in the tree.
        # otherwise, return False.
        # you may use a helper method __find_node() to find a particular node with the data value and return that node
        is_in = self.__find_node(data)
        if is_in is not None:
            return True
        else:
            return False

    def __iter__(self):
        # iterate over the nodes with inorder traversal using a for loop
        return self.inorder()

    def inorder(self):
        # inorder traversal : (LEFT, ROOT, RIGHT)
        return self.__traverse(self.root, Tree.INORDER)

    def preorder(self):
        # preorder traversal : (ROOT, LEFT, RIGHT)
        return self.__traverse(self.root, Tree.PREORDER)

    def postorder(self):
        # postorder traversal : (LEFT, RIGHT, ROOT)
        return self.__traverse(self.root, Tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        # helper method implemented using generators
        # all the traversals can be implemented using a single method
        
        #Yield data of the correct node/s
        # "yield from" is how we perform our recursive yield(s)
        if curr_node is not None:
            if traversal_type == self.INORDER:
                yield from self.__traverse(curr_node.left, self.INORDER)
                yield curr_node.data
                yield from self.__traverse(curr_node.right, self.INORDER)
            elif traversal_type == self.PREORDER:
                yield curr_node.data
                yield from self.__traverse(curr_node.left, self.PREORDER)
                yield from self.__traverse(curr_node.right, self.PREORDER)
            else:
                yield from self.__traverse(curr_node.left, self.POSTORDER)
                yield from self.__traverse(curr_node.right, self.POSTORDER)
                yield curr_node.data

    def find_successor(self, data):
        """Finds the node with the smallest key greater than
        the key of the input node.
        
        Raises KeyError if the input node is not in the tree"""
        # Find the successor node
        # If the value specified by find_successor does NOT exist in the tree, then raise a KeyError
        # helper method to implement the delete method but may be called on its own
        # If the right subtree of the node is nonempty,then the successor is just 
        # the leftmost node in the right subtree.
        # If the right subtree of the node is empty, then go up the tree until a node that is
        # the left child of its parent is encountered. The parent of the found node will be the
        # successor to the initial node.
        # Note: Make sure to handle the case where the parent is None
        """Accounts for both cases where parent is None (data is root) by first checking if the
        current node does not have a right subtree (then the root is the max and there is no
        successor), then checking if current node DOES has a right subtree (then successor is
        leftmost node in right subtree)"""
    	# Return object of successor if found else return None
        curr = self.__find_node(data)
        try:
            if curr is None:
                raise KeyError
        except KeyError:
            print("Error: Input node not found in tree")
            raise KeyError
        else:
            # if current node is largest in the tree, it has no successor
            if curr.data == self.max():
                return None
            # if current node has right child, successor is smallest
            # (leftmost) node in right subtree
            if curr.right is not None:
                curr = curr.right
                while curr.left is not None:
                    curr = curr.left
                return curr
            # if neither of those returned, and current node is parent's
            # right child, current node is rightmost node in left subtree and
            # successor is the root node
            succ = curr.parent
            while succ is not None and curr == succ.right:
                curr = succ
                succ = succ.parent
            return succ

    def delete(self, data):
        """Finds the node defined by the input data, splices it out
        of the tree, and shifts other nodes in such a way to satisfy BST
        properties.
        
        Raises KeyError if the input node is not in the tree."""
        # Find the node to delete.
        # If the value specified by delete does NOT exist in the tree, then don't change the tree and raise a KeyError
        # If you find the node and ...
        #  a) The node has no children, just set it's parent's pointer to None.
        #  b) The node has one child, make the nodes parent point to its child.
        #  c) The node has two children, replace it with its successor, and remove
        #       successor from its previous location.
        # Recall: The successor of a node is the left-most node in the node's right subtree.
        # Note: Make sure to handle the case where the parent is None

        out = self.__find_node(data)
        try:
            if out is None:
                raise KeyError
        except KeyError:
            print("Error: Node to delete not found in tree")
            raise KeyError
        else:
            # y represents the location of the node we're splicing out
            # if our input node has 2 children, swap input node with y (its successor)
            # to ensure BST property is maintained
            y = None
            # x is the child of y, or None if no child
            x = None
            # determine node y to splice out
            # out itself if it has 0 or 1 children
            # successor if it has 2 children
            if out.left is None or out.right is None:
                y = out
            else:
                y = self.find_successor(data)
            
            # if y == out, then y has <= 1 children
            # if y == successor, y also has 1 child (and no left child)
            if y.left is not None:
                x = y.left
            else:
                x = y.right

            # splice out y, moving its child up
            if x is not None:
                x.parent = y.parent
            if y.parent is None:
                self.root = x
            elif y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x
            # new tree is constructed with temporary y node effectively removed
            # turn out (actual node we want to delete) into y by copying y's data
            # into out
            if y != out:
                out.data = y.data
            # now out no longer exists in the tree