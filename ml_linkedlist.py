#multilevel linkedlist
class Node:
    def __init__(self, data):
        self.data = data
        self.level = None
        self.down = None

    def get_level(self):
        return self.level

    def get_down(self):
        return self.down

    def get_data(self):
        return self.data

    def set_level(self, new_node):
        self.level = new_node

    def set_down(self, new_node):
        self.down = new_node

class Multilevel_LinkedList:
    def __init__(self):
        self.top = None

    def insert_level(self, data):
        new_node = Node(data)
        new_node.set_level(self.top)
        self.top = new_node

    def print_list(self):
        current = self.top
        while current:
            print current.get_data()
            current = current.get_level()

def main():
    ml = Multilevel_LinkedList()
    ml.insert_level("56")
    ml.insert_level("8")
    ml.insert_level("78")
    ml.insert_level("4")

    ml1 = Multilevel_LinkedList()
    ml1.insert_level("90")
    ml1.insert_level("23")
    ml1.insert_level("91")
    ml1.insert_level("45")

    ml.print_list()
    print
    ml1.print_list()

    ml.top.down = ml1.top #assigning a down of one of the nodes to other llist appearing below
    print
    print ml.top.get_data(), ml.top.level.get_data(),\
          ml.top.down.get_data(), ml.top.down.level.get_data()


if __name__ == "__main__":
    main()
