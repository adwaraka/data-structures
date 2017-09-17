class Stack:
    def __init__(self, stack):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack)-1]

    def print_stack(self):
        print
        for i in self.stack:
            print i, 

def main():
    s = Stack([])
    s.push(1)
    s.push(17)
    s.pop()
    s.push(11)
    s.push(41)
    s.push(15)
    s.print_stack()
    s.pop()
    s.push(42)
    s.push(55)
    s.print_stack()
    s.pop()
    print
    print s.peek()

if __name__ == "__main__":
    main()