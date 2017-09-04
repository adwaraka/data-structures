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

def main():
    N = int(raw_input())
    arr = map(int, raw_input().split(" "))
    root = Node(arr[0])
    for i in xrange(1, N):
        n = Node(arr[i])
        insert(root, n)
    inorder(root)

if __name__ == "__main__":
    main()