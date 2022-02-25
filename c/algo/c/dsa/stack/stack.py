# stack implementation using a linked list.
import sys
 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
 
class Stack:
 
    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.head = Node("head")
        self.size = 0
 
    # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]
 
    # Get the current size of the stack
    def getSize(self):
        return self.size
 
    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0
 
    # Get the top item of the stack
    def peek(self):
 
        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value
 
    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
 
    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value
 
 
if __name__ == "__main__":
    if(len(sys.argv) < 2):
        exit(0)

    count = int(sys.argv[1])
    debug = False
    if(len(sys.argv) > 2):
        if(sys.argv[2] == '-d'):
            debug = True

    step = 1
    for i in range(1, len(str(count))-1):
            step = step * 10

    stack = Stack()
    for i in range(1, count):
        stack.push(i)

    if debug:
        print("Stack: {}".format(stack))
 
    for i in range(1, count):
        remove = stack.pop()
        if((i < 10) or (i%step == 0)):
            print("Pop: {}".format(remove))

    if debug:
        print("Stack: {}".format(stack))


