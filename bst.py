# Binary Search Tree


class NewNode:
    def __init__(self, new_data):
        self.data = new_data
        self.left = None
        self.right = None

    def print_node(self):
        print(self.data, end=" ")


class BST:
    def __init__(self):
        self.root = None

    def insert_node(self, new_data):
        node = NewNode(new_data)
        if not self.root:
            self.root = node
        else:
            cp = self.root
            pp = self.root
            while cp:
                pp = cp
                if cp.data < new_data:
                    cp = cp.right
                else:
                    cp = cp.left
            if pp.data < new_data:
                pp.right = node
            else:
                pp.left = node

    def largest_in_left(self, cp):
        cp = cp.left
        while cp:
            pp = cp
            cp = cp.right
        return pp

    def smallest_in_right(self, cp):
        cp = cp.right
        while cp:
            pp = cp
            cp = cp.left
        return pp

    def delete_node(self, old_data):
        cp = self.root
        pp = None
        pp_dir = None
        while cp:
            if cp.data < old_data:
                pp = cp
                pp_dir = True
                cp = cp.right
            elif cp > old_data:
                pp = cp
                pp_dir = False
                cp = cp.left
            else:
                # node found
                if cp.left and cp.right:
                    # 2nd degree node
                    rp = largest_in_left(cp)
                    cp.data = rp.data
                    delete_by_node(self, rp)
                elif cp.left:




    def search(self, new_data):
        cp = self.root
        while cp:
            if cp.data == new_data:
                return cp
            elif cp.data < new_data:
                cp = cp.right
            else:
                cp = cp.left
        return False

    def preorder(self, cp):
        if not cp:
            return
        cp.print_node()
        self.preorder(cp.left)
        self.preorder(cp.right)

    def inorder(self, cp):
        if not cp:
            return
        self.inorder(cp.left)
        cp.print_node()
        self.inorder(cp.right)

    def postorder(self, cp):
        if not cp:
            return
        self.postorder(cp.left)
        self.postorder(cp.right)
        cp.print_node()

    def levelorder(self, cp):
        q = [cp]
        while q:
            node = q.pop(0)
            node.print_node()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


if __name__ == "__main__":
    data = [8,2,3,1,114,0,-4,17,16,6,9,10,13]
    search_data = [-4,3,10,4,114]

    t = BST()
    for d in data:
        t.insert_node(d)
    #t.print_tree()

    for d in search_data:
        if t.search(d):
            print("%d found" % d)
        else:
            print("%d not found" % d)

    root = t.root
    t.preorder(root)
    print("")
    t.inorder(root)
    print("")
    t.postorder(root)
    print("")
    t.levelorder(root)
    print("")
