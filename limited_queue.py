#CONSTRUCTING A QUEUE WHICH USES A FIXED-LENGTH ARRAY
class QueueNode:
    
    def __init__(self):
        self.queue = []
        self.next = None

class QueueOps:
    
    def __init__(self):
        self.start_queue = None
        self.currentQueue = None
 
    def enqueue(self, element):
        if self.start_queue is None:
            self.start_queue = QueueNode()
            self.currentQueue = self.start_queue
            self.currentQueue.queue.append(element)
            self.start_queue.next = None
            self.currentQueue.next = None
        elif len(self.currentQueue.queue) == 5:
            new_queue = QueueNode()
            new_queue.queue.append(element)
            self.currentQueue.next = new_queue
            self.currentQueue = new_queue
        else:
            self.currentQueue.queue.append(element)
            
    def print_all(self):
        pointer = self.start_queue
        while pointer:
            print pointer.queue
            pointer = pointer.next

    #TODO deque

q = QueueOps()
for i in range(33):
    q.enqueue(i)
q.print_all()
