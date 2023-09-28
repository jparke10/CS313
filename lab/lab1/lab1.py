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
        self.__data = data
        self.__next_node = next_node

    def setData(self, data):
        '''Set the "data" data field to the corresponding input.'''
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
    """This class represents a linked-list queue data structure, which is
    open at both ends and uses a first-in first-out operation order."""
    def __init__(self):
        self.__head = None
        self.__tail = None

    def __str__(self):
        '''Loop through your queue and print each Node's data.'''
        try:
            if self.isEmpty():
                raise AttributeError
        except AttributeError:
            print("Error: Attempted to print queue, but queue was empty!")
            raise AttributeError
        else:
            current_node = self.__head
            queue_print = '['
            while current_node != None:
                queue_print += str(current_node.getData())
                # no trailing whitespace for last element
                if current_node.getNext() != None:
                    queue_print += ", "
                current_node = current_node.getNext()
            return queue_print + ']'

    def enqueue(self, newData):
        '''Create a new node whose data is newData and whose next node is null
        Update head and tail.'''
        # Hint: Think about what's different for the first node added to the Queue
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
    """This class represents a linked-list stack data structure, which is
    open at the top and uses a last-in first-out operation order."""
    def __init__(self):
        ''' We want to initialize our Stack to be empty.
        (ie) Set top as null'''
        self.__top = None

    def __str__(self):
        '''Loop through your stack and print each Node's data.'''
        try:
            if self.isEmpty():
                raise AttributeError
        except AttributeError:
            print("Error: Tried to print stack, but the stack was empty!")
            raise AttributeError
        else:
            current_node = self.__top
            stack_print = '['
            while current_node != None:
                stack_print += str(current_node.getData())
                # no trailing whitespace for last element
                if current_node.getNext() != None:
                    stack_print += ", "
                current_node = current_node.getNext()
            return stack_print + ']'

    def push(self, newData):
        '''We want to create a node whose data is newData and next node is top.
        Push this new node onto the stack
        Update top'''
        new_node = Node(newData)
        if self.isEmpty():
            self.__top = new_node
        else:
            new_node.setNext(self.__top)
            self.__top = new_node

    def pop(self):
        ''' Return the Node that currently represents the top of the stack.
        Update top'''
        # Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #         to hold important information
        # Hint: Return null on a empty stack
        # Hint: Return the element(data) that is popped
        try:
            if self.isEmpty():
                raise AttributeError
        except AttributeError:
            print("Error: Attempted a pop, but the stack was empty!")
            raise AttributeError
        else:
            popped = self.__top
            self.__top = self.__top.getNext()
            return popped.getData()

    def isEmpty(self):
        '''Check if the Stack is empty.'''
        return self.__top == None


def isPalindrome(s):
    '''Use your Queue and Stack class to test wheather an input is a palindrome.'''
    assert isinstance(s, str)
    myStack = Stack()
    myQueue = Queue()

    ## Helper function ##
    # print("stack data")
    # myStack.printStack()

    # print("queue data")
    # myQueue.printQueue()

    # normalize string for palindrome check - strip spaces, capitals
    normal = s.lower()
    normal = normal.replace(' ', '')
    length = len(normal)

    # queue implementation
    for char in normal:
        myQueue.enqueue(char)
    for i in range(1, ((length + 1) / 2).__ceil__()):
        if normal[-i] != myQueue.dequeue():
            return False
        
    # stack implementation
    for char in normal:
        myStack.push(char)
    for i in range(((length + 1) / 2).__ceil__()):
        if normal[i] != myStack.pop():
            return False

    # Return appropriate value, if no non-palindromes found
    return True

def isPalindromeEC(s):
    '''Implement if you wish to do the extra credit.'''

    # Return appropriate value
    return
