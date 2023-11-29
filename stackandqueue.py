class Stack:
    #stack implementation using pyton list
    def __init__(self):
        self.arr = []
        self.top_of_stack = -1
        
    def push(self,x):
        self.arr.append(x)
        self.top_of_stack += 1
    
    def pop(self):
        if self.top_of_stack == -1:
            return 'Empty'
        self.top_of_stack -=1
        return self.arr.pop()
    
    def is_empty(self):
        if self.top_of_stack == -1:
            return True
        return False

    def size(self):
        return self.top_of_stack+1
    
class Queue:
    #queue implementation using python lists
    def __init__(self):
        self.arr = []
    
    def enqueue(self, data):
        self.arr.append(data)
    
    def dequeue(self):
        if len(self.arr) == 0:
            return 'Empty'
        v = self.arr[0]
        self.arr = self.arr[1:]
        return v
    
    def size(self):
        return len(self.arr)

class Deque:
    def __init__(self):
        self.arr =[]
        
    def enqueue_start(self, x):
        self.arr = [x] + self.arr
    
    def enqueue(self, x):
        self.arr += [x]
    
    def dequeue(self):
        if len(self.arr) == 0:
            return 'Empty'
        v = self.arr[0]
        self.arr = self.arr[1:]
        return v
    
    def dequeue_last(self):
        if len(self.arr) ==0:
            return 'Empty'
        v = self.arr[-1]
        self.arr = self.arr[:-1]
        return v
    
    def size(self):
        return len(self.arr)

class QueueStack:
    #queue implementation using two stacks
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    
    def enqueue(self, data):
        while(not self.s1.is_empty()):
            k = self.s1.pop()
            self.s2.push(k)
        self.s1.push(data)
        while(not self.s2.is_empty()):
            k = self.s2.pop()
            self.s1.push(k)
    
    def dequeue(self):
        return self.s1.pop()
    
    def size(self):
        return self.s1.size()

class StackQueue:
    #stack implementation using queues
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        
    def push(self,x):
        self.q2.enqueue(x)
        while(self.q1.size() !=0):
            k = self.q1.dequeue()
            self.q2.enqueue(k)
        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self):
        return self.q1.dequeue()
    
    def is_empty(self):
        return self.q1.size == 0

    def size(self):
        return self.q1.size()
    
    def print_stack(self):
        print(self.q1.arr)