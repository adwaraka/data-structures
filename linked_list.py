#             head
#              |
#              |
#              V
#  4, 9, 9, 8, 1

class Node():
    def __init__(self, data=None, node=None):
        self.data = data
        self.node = node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.node

    def set_next(self, new_node):
        self.node = new_node
        

class SingleLinkedList():
    def __init__(self, data=None):
        self.top = data

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.top)
        self.top = new_node #set the top to the new node added at the end

    def search(self, data):
        current = self.top
        while current:
            if current.get_data() == data:
                print "Found"
                break
            else:
                current = current.get_next()

    def delete(self, data):
        current = self.top
        previous = None
        while current:
            if current.get_data() == data:
                break
            else:
                previous = current #pointing prev where current is before current moves to the next
                current = current.get_next()
        if current is None:
            print "Node not found"
        if previous is None:
            self.top = current.get_next() #the top node it self
        else:
            previous.set_next(current.get_next())
            
    def print_list(self):
        current = self.top
        while current:
            print current.get_data()
            current = current.get_next()

def main():
    list = SingleLinkedList()
    list.insert("4")
    list.insert("15")
    list.insert("5")
    list.insert("11")
    list.insert("19")
    list.insert("9")
    list.delete("5")
    list.print_list()

if __name__ == "__main__":
    main()