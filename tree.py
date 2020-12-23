class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            
            p = p.parent
            level = level+1
        
        return level

    def print_Tree(self):
        spaces = ' ' * self.get_level() * 3
        print(spaces + self.data)
        if self.children:
            for child in self.children:
                child.print_Tree()
        

def build_tree():
    root = TreeNode("Electronics") #define root first this is the head node

    laptop = TreeNode("Laptop") 
    laptop.add_child(TreeNode("MSI"))
    laptop.add_child(TreeNode("Apple"))
    laptop.add_child(TreeNode("Asus"))

    Cellphone = TreeNode("Phones")
    Cellphone.add_child(TreeNode("samsung"))
    Cellphone.add_child(TreeNode("IOS"))
    Cellphone.add_child(TreeNode("blackberry"))

    tv = TreeNode("Television")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Hisense"))
    tv.add_child(TreeNode("TLC"))

    root.add_child(laptop)
    root.add_child(Cellphone)
    root.add_child(tv)

    return root

root = build_tree()
root.print_Tree()
print("*****")
