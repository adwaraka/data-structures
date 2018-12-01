#5
#5 4 9 0 2
#0 2 4 5 9
class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        return self.data

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print root.get_data(),
        inorder(root.right)

def preorder(root):
    if root is not None:
        print root.get_data(),
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print root.get_data(),

def maxDepth(node):
    if node is None:
        return 0
    else :
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1

def main():
    N = int(raw_input())
    arr = map(int, raw_input().split(" "))
    root = Node(arr[0])
    for i in xrange(1, N):
        n = Node(arr[i])
        insert(root, n)
    print "Inorder"
    inorder(root)
    print "\nPreorder"
    preorder(root)
    print "\nPostorder"
    postorder(root)
    print "\nHeight:",
    print maxDepth(root)

if __name__ == "__main__":
    main()
