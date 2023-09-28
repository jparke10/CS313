class Node(object):
    """
    A class to represent a node.

    ...

    Attributes
    ----------
    data : int or float
        An individual character or number to be stored in a node
    next_node : object of class Node
        A pointer to the next node in a stack or queue

    Methods
    -------
    setData(data):
        Updates the value of data attribute of Node
    setNext(next_node):
        Updates the value of next_node attribute of Node
    getData():
        Returns the value of data attribute
    getNext():
        Returns the value of next_node attribute
    """
    def __init__(self, data = None, next_node = None):
        """
        Constructs (or initializes) the attributes for an object of the class

        ...

        Parameters
        ----------
        data : int or float
            An individual character or number to be stored in a node
        next_node : object of class Node
            A pointer to the next node in a stack or queue

        """
        assert isinstance(data, int) or isinstance(data, float) or data == None
        assert isinstance(next_node, Node) or next_node == None
        self.__data = data
        self.__next_node = next_node

    def setData(self, data):
        '''Set the "data" data field to the corresponding input.'''
        assert isinstance(data, float) or isinstance(data, int)
        self.__data = data

    def setNext(self, next_node):
        '''Set the "next_node" data field to the corresponding input.'''
        assert isinstance(next_node, Node)
        self.__next_node = next_node

    def getData(self):
        '''Return the "data" data field.'''
        return self.__data

    def getNext(self):
        '''Return the "next_node" data field.'''
        return self.__next_node

class Queue(object):
    """Provide class dosctring"""
    def __init__(self):
        self.__head = None
        self.__tail = None

    def __str__(self):
        '''Loop through your queue and print each Node's data.'''
        try:
            if self.isEmpty():
                raise ValueError
        except ValueError:
            print("Error: Attempted to print queue, but queue was empty!")
            raise ValueError
        else:
            current_node = self.__head
            queue_print = "["
            while current_node != None:
                queue_print += str(current_node.getData())
                if current_node.getNext() != None:
                    queue_print += ", "
                current_node = current_node.getNext()
            queue_print = queue_print.strip()
            queue_print += "]"
            return queue_print
            

    def enqueue(self, newData):
        '''Create a new node whose data is newData and whose next node is null
        Update head and tail.'''
        # Hint: Think about what's different for the first node added to the Queue
        assert isinstance(newData, float) or isinstance(newData, int)
        new_node = Node(newData)
        if self.isEmpty():
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.setNext(new_node)
            self.__tail = new_node


    def dequeue(self):
        '''Return the head of the Queue
        Update head.'''
        #  Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #          to hold important information
        #  Hint: Return null on a empty Queue
        # Hint: Return the element(data) that is dequeued.
        try:
            if self.isEmpty():
                raise AttributeError
        except AttributeError:
            print("Error: Attempted a dequeue, but the queue was empty!")
            raise AttributeError
        else:
            dequeued = self.__head
            self.__head = self.__head.getNext()
            # set queue empty if removing last element from queue
            if self.__head == None:
                self.__tail = None
            return dequeued.getData()

    def isEmpty(self):
        '''Check if the Queue is empty.'''
        return self.__head == None and self.__tail == None


class Stack(object):
    """Provide class dosctring"""
    def __init__(self):
        ''' We want to initialize our Stack to be empty.
        (ie) Set top as null'''

    def __str__(self):
        '''Loop through your stack and print each Node's data.'''
        pass

    def push(self, newData):
        '''We want to create a node whose data is newData and next node is top.
        Push this new node onto the stack
        Update top'''
        pass

    def pop(self):
        ''' Return the Node that currently represents the top of the stack.
        Update top'''
        # Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #         to hold important information
        # Hint: Return null on a empty stack
        # Hint: Return the element(data) that is popped
        pass

    def isEmpty(self):
        '''Check if the Stack is empty.'''
        pass


def isPalindrome(s):
    '''Use your Queue and Stack class to test wheather an input is a palindrome.'''
    myStack = Stack()
    myQueue = Queue()

    ## Helper function ##
    # print("stack data")
    # myStack.printStack()

    # print("queue data")
    # myQueue.printQueue()

    # Return appropriate value
    return

def isPalindromeEC(s):
    '''Implement if you wish to do the extra credit.'''

    # Return appropriate value
    return
