import sys
n= int(sys.stdin.readline().rstrip())

class deque : 
    def __init__(self) : 
        self.front = 0
        self.rear = 0
        self.items = [None]*n
    
    def is_Full(self) : 
        return self.front == (self.rear+1) % n 
    
    def is_Empty(self) : 
        return self.front == self.rear
    #push_front
    def push_front(self,item) :
        if not self.is_Full() : 
            self.items[self.front] = item
            self.front = (self.front-1 +n) % n
    #push_back
    def push_back(self,item) : 
        if not self.is_Full() : 
            self.items.append(item)
    #pop_front
    def pop_front(self,item) : 
        if not self.is_Empty() : 
            self.front = (self.front+1) %n
            print(self.items[self.front])
            self.items[self.front] = None
        else:
            print("-1")
    #pop_back
    def pop_back(self,item) : 
        if not self.is_Empty() : 
            print(self.items[self.rear])
            self.items[self.rear] = None
            self.rear = (self.rear-1+n) % n
        else:
            print("-1")
    
    def size(self) : 
        return (self.rear-self.front+n)%n
    
    
    def empty(self) :
        if self.front == self.rear :
            print("1")
        else:
            print("0")

    def front(self) : 
        if not self.is_Empty : 
            print(self.items[(self.front+1)%n])
        else : 
            print("-1")
    
    def back(self) : 
        if not self.is_Empty : 
            print(self.items[self.rear])
        else : 
            print("-1")

    
q = deque()



    