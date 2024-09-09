"""
Implement Stack using arrays

we have three methods for stack :
push ,pop and top
"""
class Stack:

    def __init__(self):
        self.top = -1
        self.size = 0
        self.arr = []



    def push(self,val):
        self.size+=1
        self.top+=1
        self.arr.append(val)


    def pop(self):
        self.size-=1
        x= self.arr[self.top]
        self.top-=1

        return x


    def top(self):
        return self.arr[self.top]

    def len(self):
        return self.size

    def get_stack(self):
        return self.arr




s = Stack()

s.push(1)
s.push(2)

print(s.len())

