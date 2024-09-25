class Queue:
    def __init__ (self, size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.queue = [0] * self.size

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:  
            print("Overflow")
        elif self.front == -1:  
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:  
            print("Underflow")
        elif self.front == self.rear:  
            print(self.queue[self.front])
            self.front = self.rear = -1  
        else:
            print(self.queue[self.front])
            self.front = (self.front + 1) % self.size

    def display(self):
        if self.front == -1:  
            print("Queue is empty")
        else:
            i = self.front
            while True:
                print(self.queue[i], end=" -> ")
                if i == self.rear:
                    break
                i = (i + 1) % self.size
            print(None)

size = int(input("Enter the number of elements: "))
Q = Queue(size)
for i in range(size):
    data = int(input("Enter the data: "))
    Q.enqueue(data)
Q.display()
Q.dequeue()
Q.display()
Q.dequeue()
Q.enqueue(10)
Q.enqueue(10)
Q.display()