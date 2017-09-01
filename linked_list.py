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

    def print_list(self):
        current = self.top
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
    list.search("1")
    list.search("-1")
    list.search("9")

if __name__ == "__main__":
    main()