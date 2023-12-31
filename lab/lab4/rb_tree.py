class Node(object):
    def __init__(self, data, left = None, right = None, parent = None, color = 'red'):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        # Color can be string containing 'black' or 'red'
        self.color = color


class rb_tree(object):
    """Red-black tree
    
    A standard binary search tree with extra attributes and methods
    to ensure a self-balancing property is maintained, to allow for
    more efficient worst-case search, insert and delete operations.
    
    Attributes
    ----------
    root : Node
        The root of the tree, initially defined as None and filled in
        by tree operations. Worth noting that type Node has a new attribute,
        color, which is always set to 'black' at the root node to maintain
        red-black properties.
        
    sentinel : Node
        A special type of node which serves as a pointer for 'null-leaf' nodes
        of the tree. Serves as a placeholder for methods such as rb_insert_fixup
        to check null leaf nodes, as NoneType would throw exceptions.
        
    New Methods
    -----------
    insert(data):
        Similar to bst_insert(), with an appropriate call to __rb_insert_fixup(1)
        to ensure red-black property is maintained. Newly inserted nodes are always
        red by default.
    delete(data):
        Similar to standard BST delete(), with a call to __rb_delete_fixup(1) when
        appropriate (in the event the deleted node was originally black) to ensure
        red-black property is maintained.
    left_rotate(current_node), right_rotate(current_node):
        Rotations contribute to self-balancing property of red-black trees by modifying
        pointers to nodes. Height of subtree can be increased or decreased with rotation
        operations.
    __rb_insert_fixup(z):
        Restores red-black properties of the tree after a new insertion by color shifting
        and rotating nodes where appropriate.
    __rb_delete_fixup(x):
        Restores red-black properties of the tree after deletion of a black node by color
        shifting and rotating nodes where appropriate.
    """
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3
    # initialize root and size
    def __init__(self):
        self.root = None
        self.sentinel = Node(None, color = 'black')
        self.sentinel.parent = self.sentinel
        self.sentinel.left = self.sentinel
        self.sentinel.right = self.sentinel
    
    def print_tree(self):
        # Print the data of all nodes in order
        self.__print_tree(self.root)
    
    def __print_tree(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        # Printed in preorder
        if curr_node is not self.sentinel:
            print(str(curr_node.data), end=' ')  # save space
            self.__print_tree(curr_node.left)
            self.__print_tree(curr_node.right)

    def __print_with_colors(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        # Printed in PREORDER
        # Extracts the color of the node and print it in the format -dataC- where C is B for black and R for red
        if curr_node is not self.sentinel:

            if curr_node.color is "red":
                node_color = "R"
            else:
                node_color = "B"

            print(str(curr_node.data)+node_color, end=' ')  # save space
            self.__print_with_colors(curr_node.left)
            self.__print_with_colors(curr_node.right)

    def print_with_colors(self):
        # Also prints the data of all node but with color indicators
        self.__print_with_colors(self.root)
            
            
    def __iter__(self):
        return self.inorder()

    def inorder(self):
        return self.__traverse(self.root, rb_tree.INORDER)

    def preorder(self):
        return self.__traverse(self.root, rb_tree.PREORDER)

    def postorder(self):
        return self.__traverse(self.root, rb_tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        if curr_node is not self.sentinel:
            if traversal_type == self.PREORDER:
                yield curr_node
            yield from self.__traverse(curr_node.left, traversal_type)
            if traversal_type == self.INORDER:
                yield curr_node
            yield from self.__traverse(curr_node.right, traversal_type)
            if traversal_type == self.POSTORDER:
                yield curr_node

    # find_min travels across the leftChild of every node, and returns the
    # node who has no leftChild. This is the min value of a subtree
    def find_min(self):
        current_node = self.root
        while current_node.left:
            current_node = current_node.left
        return current_node
    
    # find_node expects a data and returns the Node object for the given data
    def find_node(self, data):
        if self.root:
            res = self.__get(data, self.root)
            if res:
                return res
            else:
                raise KeyError('Error, data not found')
        else:
            raise KeyError('Error, tree has no root')

    # helper function __get receives a data and a node. Returns the node with
    # the given data
    def __get(self, data, current_node):
        if current_node is self.sentinel: # if current_node does not exist return None
            print("couldnt find data: {}".format(data))
            return None
        elif current_node.data == data:
            return current_node
        elif data < current_node.data:
            # recursively call __get with data and current_node's left
            return self.__get( data, current_node.left )
        else: # data is greater than current_node.data
            # recursively call __get with data and current_node's right
            return self.__get( data, current_node.right )
    

    def find_successor(self, data):
        # Private Method, can only be used inside of BST.
        current_node = self.find_node(data)

        if current_node is self.sentinel:
            raise KeyError

        # Travel left down the rightmost subtree
        if current_node.right:
            current_node = current_node.right
            while current_node.left is not self.sentinel:
                current_node = current_node.left
            successor = current_node

        # Travel up until the node is a left child
        else:
            parent = current_node.parent
            while parent is not self.sentinel and current_node is not parent.left:
                current_node = parent
                parent = parent.parent
            successor = parent

        if successor:
            return successor
        else:
            return None

    # put adds a node to the tree
    def insert(self, data):
        # if the tree has a root
        if self.root:
            # use helper method __put to add the new node to the tree
            new_node = self.__put(data, self.root)
            self.__rb_insert_fixup(new_node)
        else: # there is no root
            # make root a Node with values passed to put
            self.root = Node(data, parent = self.sentinel, left = self.sentinel, right = self.sentinel)
            new_node = self.root
            self.__rb_insert_fixup(new_node)
    
    #Insertion for Binary Search Tree
    def bst_insert(self, data):
        # if the tree has a root
        if self.root:
            # use helper method __put to add the new node to the tree
            self.__put(data, self.root)
        else: # there is no root
            # make root a Node with values passed to put
            self.root = Node(data, parent = self.sentinel, left = self.sentinel, right = self.sentinel)
        
    # helper function __put finds the appropriate place to add a node in the tree
    def __put(self, data, current_node):
        if data < current_node.data:
            if current_node.left != self.sentinel:
                new_node = self.__put(data, current_node.left)
            else: # current_node has no child
                new_node = Node(data,
                parent = current_node,
                left = self.sentinel,
                right = self.sentinel )
                current_node.left = new_node
        else: # data is greater than or equal to current_node's data
            if current_node.right != self.sentinel:
                new_node = self.__put(data, current_node.right)
            else: # current_node has no right child
                new_node = Node(data,
                parent = current_node,
                left = self.sentinel,
                right = self.sentinel )
                current_node.right = new_node
        return new_node

    
    def delete(self, data):
        # Same as binary tree delete, except we call rb_delete fixup at the end.
        z = self.find_node(data)
        try:
            if z is None:
                raise KeyError
        except KeyError:
            print("Error: Node to delete not found in tree")
            raise KeyError
        else:
            y = z
            y_original_color = y.color
            if z.left == self.sentinel:
                x = z.right
                # replace z by its right child
                if z.parent == self.sentinel:
                    self.root = x
                elif z == z.parent.left:
                    z.parent.left = x
                else:
                    z.parent.right = x
                x.parent = z.parent
            elif z.right == self.sentinel:
                x = z.left
                # replace z by its left child
                if z.parent == self.sentinel:
                    self.root = x
                elif z == z.parent.left:
                    z.parent.left = x
                else:
                    z.parent.right = x
                x.parent = z.parent
            else:
                # else, y is z's successor
                y = self.find_successor(z.data)
                y_original_color = y.color
                x = y.right
                # is y farther down the tree?
                if y != z.right:
                    # replace y by its right child
                    if y.parent == self.sentinel:
                        self.root = x
                    elif y == y.parent.left:
                        y.parent.left = x
                    else:
                        y.parent.right = x
                    x.parent = z.parent
                    # z's right child becomes y's right child
                    y.right = z.right
                    y.right.parent = y
                # in case x is self.sentinel
                else:
                    x.parent = y
                # replace z by its successor y
                if z.parent == self.sentinel:
                    self.root = y
                elif z == z.parent.left:
                    z.parent.left = y
                else:
                    z.parent.right = y
                y.parent = z.parent
                # give z's left child to y, which had no left child
                y.left = z.left
                y.left.parent = y
                y.color = z.color
            # correct red-black violations if they occurred
            if y_original_color == 'black':
                self.__rb_delete_fixup(x)
        

    def left_rotate(self, current_node):
        # If there is nothing to rotate with, then raise a KeyError
        # if x is the root of the tree to rotate with left child subtree T1 and right child y, 
        # where T2 and T3 are the left and right children of y then:
        # x becomes left child of y and T3 as its right child of y
        # T1 becomes left child of x and T2 becomes right child of x

        # refer page 328 of CLRS book for rotations
        try:
            y = current_node.right
            if y is None or y == self.sentinel:
                raise KeyError
        except KeyError:
            print("Error: Tried to left rotate, but no child to rotate with")
            raise KeyError
        else:
            # turn y's left subtree into current_node's right subtree
            current_node.right = y.left
            # if y's left subtree is not empty, current_node becomes parent
            # of subtree's root
            if y.left != self.sentinel:
                y.left.parent = current_node
            # current_node's parent becomes y's parent
            y.parent = current_node.parent
            # if current_node was the root, y becomes the root
            if current_node.parent is self.sentinel:
                self.root = y
            # otherwise, if current_node was a left child, y becomes
            # a left child
            elif current_node == current_node.parent.left:
                current_node.parent.left = y
            # otherwise, current_node was a right child, and now y is
            else:
                current_node.parent.right = y
            # make current_node become y's left child
            y.left = current_node
            current_node.parent = y
    
    def right_rotate(self, current_node):
        # If there is nothing to rotate with, then raise a KeyError
        # If y is the root of the tree to rotate with right child subtree T3 and left child x, 
        # where T1 and T2 are the left and right children of x then:
        # y becomes right child of x and T1 as its left child of x
        # T2 becomes left child of y and T3 becomes right child of y

        # refer page 328 of CLRS book for rotations
        # symmetrical to left_rotate
        try:
            y = current_node.left
            if y is None or y == self.sentinel:
                raise KeyError
        except KeyError:
            print("Error: Tried to right rotate, but no child to rotate with")
            raise KeyError
        else:
            current_node.left = y.right
            if y.right != self.sentinel:
                y.right.parent = current_node
            y.parent = current_node.parent
            if current_node.parent is self.sentinel:
                self.root = y
            elif current_node == current_node.parent.left:
                current_node.parent.left = y
            else:
                current_node.parent.right = y
            y.right = current_node
            current_node.parent = y

    
    def __rb_insert_fixup(self, z):
        # This function maintains the balancing and coloring property after bst insertion into
        # the tree. Please red the code for insert() method to get a better understanding
        # refer page 330 of CLRS book and lecture slides for rb_insert_fixup

        while z.parent.color == 'red':
            # is z's parent a left child?
            if z.parent == z.parent.parent.left:
                # y is z's uncle (grandparent's other child)
                y = z.parent.parent.right
                # are z's parent and uncle both red?
                if y.color == 'red':
                    # case 1
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        # case 2
                        z = z.parent
                        self.left_rotate(z)
                    # case 3
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.right_rotate(z.parent.parent)
            else:
                # same as above cases, with left and right flipped
                y = z.parent.parent.left
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.left_rotate(z.parent.parent)
        self.root.color = 'black'

    def __rb_delete_fixup(self, x):
        # This function maintains the balancing and coloring property after bst deletion 
        # from the tree. Please read the code for delete() method to get a better understanding.
        # refer page 338 of CLRS book and lecture slides for rb_delete_fixup
        
        while x != self.root and x.color == 'black':
            # is x a left child?
            if x == x.parent.left:
                # w is x's sibling
                w = x.parent.right
                if w.color == 'red':
                    # case 1
                    w.color = 'black'
                    w.parent.color = 'red'
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    # case 2
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        # case 3
                        w.left.color = 'black'
                        w.color = 'red'
                        self.right_rotate(w)
                        w = x.parent.right
                    # case 4
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                # same as above, with left and right swapped
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'black'


    


    
    