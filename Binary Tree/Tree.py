class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def takeInputTree():
    data = int(input())
    if data==-1:
        return None
    root = Tree(data)
    leftNode = takeInputTree()
    rightNode=takeInputTree()
    root.left=leftNode
    root.right=rightNode
    return root
    
def prePrintTree(root):
    if root is None:
        return
    print(root.data)
    prePrintTree(root.left)
    prePrintTree(root.right)

def postPrintTree(root):
    if root is None:
        return
    postPrintTree(root.left)
    postPrintTree(root.right)
    print(root.data)
    
def inPrintTree(root):
    if root is None:
        return
    inPrintTree(root.left)
    print(root.data)
    inPrintTree(root.right)
    
def printInFormate(root):
    if root is None:
        return
    print(root.data,end=": ")
    if root.left!=None:
        print("L: ",root.left.data,end=" ")
    if root.right!=None:
        print("R: ",root.right.data,end=" ")
    print()
    printInFormate(root.left)
    printInFormate(root.right)