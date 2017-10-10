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

def merge_list(head1, head2):
    new_list_head = None
    set_new_head = None
    #print head1.start.get_data(), head2.start.get_data()
    first = head1.start
    second = head2.start
    while first is not None and second is not None:
        if first.get_data() < second.get_data():
            new_node = Node(first.get_data())
            first = first.get_next()
        else:
            new_node = Node(second.get_data())
            second = second.get_next()
        if new_list_head is None:
            new_list_head = new_node
            set_new_head = new_node
        else:
            new_list_head.set_next(new_node)
        new_list_head = new_node
    if first is not None:
        while first is not None:
            new_node = Node(first.get_data())
            if new_list_head is None:
                new_list_head = new_node
                set_new_head = new_node
            else:
                new_list_head.set_next(new_node)
            new_list_head = new_node
            first = first.get_next()
    if second is not None:
        while second is not None:
            new_node = Node(second.get_data())
            if new_list_head is None:
                new_list_head = new_node
                set_new_head = new_node
            else:
                new_list_head.set_next(new_node)
            new_list_head = new_node
            second = second.get_next()
    #print the list
    current = set_new_head
    print
    while current:
        print current.get_data()
        current = current.get_next()

def main():
    l1 = SingleLinkedList()
    l1.insert("15")
    l1.insert("50")
    l1.insert("55")
    l1.print_list()
    print
    l2 = SingleLinkedList()
    l2.insert("11")
    l2.insert("19")
    l2.insert("39")
    l2.print_list()

    merge_list(l1, l2)

if __name__ == "__main__":
    main()
