class Queue:
    def __init__(self, queue):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def deque(self):
        self.queue.pop(0)

    def print_queue(self):
        print
        for i in self.queue:
            print i, 

def main():
    q = Queue([])
    q.enqueue(1)
    q.enqueue(17)
    q.deque()
    q.print_queue()
    q.enqueue(11)
    q.enqueue(41)
    q.enqueue(15)
    q.print_queue()
    q.deque()
    q.print_queue()

if __name__ == "__main__":
    main()