class Queue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, element):
        # write your code here
        self.stack2.append(element)

    def top(self):
        # write your code here
        # return the top element
        if not self.stack1:
            self.stack2to1()
        return self.stack1[-1]

    def pop(self):
        # write your code here
        # pop and return the top element
        if not self.stack1:
            self.stack2to1()
        return self.stack1.pop()
    
    def stack2to1(self):
        while self.stack2:
            value = self.stack2.pop()
            self.stack1.append(value)
            


