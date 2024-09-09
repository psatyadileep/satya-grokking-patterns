class Heap:
    def __init__(self):
        self.heap = [0]



    def push(self,val):
        self.heap.append(val)
        i = len(self.heap)-1


        #percolate up

        while self.heap[i] < self.heap[i//2]:
            self.heap[i//2], self.heap[i] = self.heap[i] , self.heap[i//2]   
            i = i//2




    def pop(self):

        if len(self.heap)==1:
            return None

        if len(self.heap)==2:
            return self.heap.pop()



        i = 1

        res = self.heap[1]

        self.heap[1]  = self.heap.pop()

        while 2*i < len(self.heap):


            right_node = self.heap[2*i+1]
            left_node = self.heap[2*i]
            if right_node and right_node<left_node and self.heap[i]>right_node:
                temp = self.heap[i]
                self.heap[i] = right_node
                right_node = temp
                i = i*2+1

            elif self.heap[i]> left_node:
                temp = self.heap[i]

                self.heap[i] = left_node
                left_node  = temp
                i = 2*1

            else:
                break

        return  res