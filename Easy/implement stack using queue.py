'''
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
'''

class MyStack(object):

    def __init__(self):
        self.queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        

    def pop(self):
        """
        :rtype: int
        push all the elements except the last one to the back of the queue 
        """
        for i in range(len(self.queue)-1):
            self.push(self.queue.popleft())
        return self.queue.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        return self.queue[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0
