print("******** PROGRAMMED BY ********")
print("****** Charlotte Quezada ******")
print("********** BSCOE 2-2 **********")
print("*** Sir Danilo Madrigalejos ***\n")

from collections import deque


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


# Test the class Queue
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
