#version 2
#start              end
#  |                 |
#  |                 |
#  V                 V
#  4, 15, 5, 11, 19, 9
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
    def __init__(self):
        self.start = None
        self.end = None

    def insert(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            self.end.set_next(new_node)
            self.end = new_node

    def print_list(self):
        current = self.start
        while current:
            print current.get_data()
            current = current.get_next()

def main():
    l = SingleLinkedList()
    l.insert("4")
    l.insert("15")
    l.insert("5")
    l.insert("11")
    l.insert("19")
    l.insert("9")
    l.print_list()

if __name__ == "__main__":
    main()
