class Treenode:
    def __init__(self,data):
        self.data=data
        self.parent=None
        self.children=[]

    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def getDepth(self):
        p=self.parent
        count=0
        while p:
            count+=1
            p=p.parent
        return count
        
    def PrintTree(self):
        prefix= "  " * self.getDepth()*3 + "|__" if self.parent else ""
        print(prefix+self.data)
        for child in self.children:
            child.PrintTree()

def CreatTree():
    root = Treenode("School_Items")

    bag = Treenode("bag")
    bag.add_child(Treenode("safari"))
    bag.add_child(Treenode("skyHigh"))
    bag.add_child(Treenode("lala"))
    notebook=Treenode("notebook")
    notebook.add_child(Treenode("classmate"))
    notebook.add_child(Treenode("BigB"))

    root.add_child(bag)
    root.add_child(notebook)

    root.PrintTree()

if __name__=="__main__":
    CreatTree()