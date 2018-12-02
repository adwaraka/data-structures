class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data)

    def inorder(self):
        if self.root is not None:
            print 'Inorder: '
            self.root.inorder()

class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.data == data:
            return False
        elif data < self.data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print str(self.data), " "
            if self.rightChild:
                self.rightChild.inorder()

    def minValueNode(self, node):
        current = node
        while(current.leftChild is not None):
            current = current.leftChild
        return current

    def delete(self, data):
        ''' For deleting the node '''
        if self is None:
            return None
        # if current node's data is less than that of root node,
        # then only search in left subtree else right subtree
        if data < self.data:
            self.leftChild = self.leftChild.delete(data)
        elif data > self.data:
            self.rightChild = self.rightChild.delete(data)
        else:
            # deleting node with one child
            if self.leftChild is None:
                temp = self.rightChild
                self = None
                return temp
            elif self.rightChild is None:
                temp = self.leftChild
                self = None
                return temp
            # deleting node with two children
            # first get the inorder successor
            temp = self.minValueNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.delete(temp.data)
        return self

def construct_tree(tree):
    tree.insert(10)
    tree.insert(12)
    tree.insert(5)
    tree.insert(4)
    tree.insert(20)
    tree.insert(8)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    tree.inorder()

if __name__ == '__main__':
    tree = Tree()
    construct_tree(tree)
    tree.delete(13)
    tree.inorder()
