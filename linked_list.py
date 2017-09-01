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
        self.head = data

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node #set the head to the new node added at the end

    def print_list(self):
        current = self.head
        while current:
            print current.get_data()
            current = current.get_next()

def main():
    list = SingleLinkedList()
    list.insert("4")
    list.insert("5")
    list.insert("1")
    list.insert("9")
    list.print_list()


if __name__ == "__main__":
    main()