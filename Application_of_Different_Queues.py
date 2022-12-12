print("******** PROGRAMMED BY ********")
print("****** Charlotte Quezada ******")
print("********** BSCOE 2-2 **********")
print("*** Sir Danilo Madrigalejos ***\n")

from collections import deque


# Building a Queue Data Type
class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()


# Test the class FIFO Queue
print("\n           * * * Queue Data Type * * *               \n")
fifo1 = Queue()
fifo1.enqueue("1st element")
fifo1.enqueue("2nd element")
fifo1.enqueue("3rd element")
print("This is the first test of FIFO Queue")
print(fifo1.dequeue())
print(fifo1.dequeue())
print(fifo1.dequeue())


fifo2 = Queue("1st element", "2nd element", "3rd element")
print("\nThis is the second test of FIFO Queue")
print("Length or Number of Elements:", len(fifo2))

for element in fifo2:
    print(element)  # This will print every element inside the variable fifo2

print("Length or Number of Elements:", len(fifo2))  # This will display 0 since the elements in the loop were consumed

# Apply the class Queue with input from user
print("\nThis is the third test of FIFO Queue")
input1 = input("Please enter the first element you want to add: ")
input2 = input("Please enter the second element you want to add: ")
input3 = input("Please enter the third element you want to add: ")

fifo3 = Queue(input1, input2, input3)
print("Length or Number of Elements:", len(fifo3))
num_input = 1
while True:
    for element in fifo3:
        print("Input No. "f"{num_input}:", element)
        num_input = num_input + 1
    break

print("Length or Number of Elements:", len(fifo3))


# Building A Stack Data Type
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()


# Test the LIFO Queue
print("\n           * * * Stack Data Type * * *               \n")
print("This is the first test of LIFO Queue")
lifo1 = Stack("1st element", "2nd element", "3rd element")

for element in lifo1:
    print(element)

# Apply LIFO Queue with list and user input
print("\nThis is the second test of LIFO Queue")
lifo2 = []
L_input1 = input("Please enter the first element you want to add: ")
L_input2 = input("Please enter the second element you want to add: ")
L_input3 = input("Please enter the third element you want to add: ")
lifo2.append(L_input1)
lifo2.append(L_input2)
lifo2.append(L_input3)

print("Third element you entered:", lifo2.pop())
print("Second element you entered:", lifo2.pop())
print("First element you entered:", lifo2.pop())


# Representing Priority Queues With a Heap
from heapq import heappush

print("\n         * * * Priority Queues With A Heap * * *             \n")
print("This is the first test of Priority Queue with Heap (heappush)")
fruits = []
heappush(fruits, "Orange")
heappush(fruits, "Apple")
heappush(fruits, "Banana")
print("This is the list of fruits:", fruits)

# Apply heappush with user input
print("\nThis is the second test of Priority Queue with Heap (heappush) and user input")
fruit_input = []
fruit_inp1 = input("Please enter the first fruit: ")
fruit_inp2 = input("Please enter the second fruit: ")
fruit_inp3 = input("Please enter the third fruit: ")
heappush(fruit_input, fruit_inp1)
heappush(fruit_input, fruit_inp2)
heappush(fruit_input, fruit_inp3)
print("This is the list of fruits you entered:", fruit_input)

from heapq import heappop
print("\nThis is the first test of Priority Queue with Heap (heappop)")
print("The fruit to be popped/removed from the list:", heappop(fruits))
print("This is the final list of fruits:", fruits)
