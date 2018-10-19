class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

def PrintPreOrderTree(array, node):
        if node is None:
            return array
        # print(node.data)
        array.append(node.data)
        if (node.left is not None):
            PrintPreOrderTree(array, node.left)
        if (node.right is not None):
            PrintPreOrderTree(array, node.right)        
        return array
    
def PrintInOrderTree(array, node):
        if node is None:
            return array
        # print(node.data)
        if (node.left is not None):
            PrintInOrderTree(array, node.left)
        array.append(node.data)
        if (node.right is not None):
            PrintInOrderTree(array, node.right)        
        return array


def PrintPostOrderTree(array, node):
        if node is None:
            return array
        # print(node.data)
        if (node.left is not None):
            PrintPostOrderTree(array, node.left)
        if (node.right is not None):
            PrintPostOrderTree(array, node.right)
        array.append(node.data)
        return array
        


def countLeaf(node):
    if node is None:
        return 0
    if (node.left is None and node.right is None):
        return 1
    else:
        return countLeaf(node.right) + countLeaf(node.right)


def isBST(node,minNumber,maxNumber):
    if node is None:
        return True
    if (node.data < minNumber or node.data > maxNumber):
        return False
    else:
        return isBST(node.left,minNumber,node.data) and isBST(node.right,node.data,maxNumber)


    
        
arrayPreOrder = []
arrayInOrder = []
arrayPostOrder = []

root = Node(10)
root.right = Node(12)
root.left = Node(9)
print (countLeaf(root))
print(PrintPreOrderTree(arrayPreOrder,root))
print(PrintInOrderTree(arrayInOrder,root))
print(PrintPostOrderTree(arrayPostOrder,root))
print(isBST(root,0 ,10000))

