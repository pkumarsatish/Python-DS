# Python Implementation for Binary Search Tree
# Available functions:
#       BST.insert_node(new_data)
#       BST.delete_node(old_data)
#       BST.largest_node(root_node)
#       BST.smallest_node(root_node)
#       BST.search(key)
#       BST.preorder/inorder/postorder
#       BST.levelorder
#
# Created by: Satish Kumar

import sys

class NewNode:
    def __init__(self, new_data):
        self.data = new_data
        self.left = None
        self.right = None
        self.level = 0

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

    def largest_node(self, cp):
        while cp:
            pp = cp
            cp = cp.right
        return pp

    def smallest_node(self, cp):
        while cp:
            pp = cp
            cp = cp.left
        return pp

    def delete_node(self, old_data, root=None):
        if not root:
            root = self.root
        cp = root
        pp = None
        pp_dir = None   # True if cp is right child of pp
        while cp:
            if cp.data < old_data:
                pp = cp
                pp_dir = True
                cp = cp.right
            elif cp.data > old_data:
                pp = cp
                pp_dir = False
                cp = cp.left
            else:
                # node found cp.data = old_data
                if cp.left and cp.right:
                    # 2nd degree node
                    rp = self.largest_node(cp.left)
                    cp.data = rp.data
                    self.delete_node(rp.data, root=cp.left)
                elif cp.left:
                    if pp_dir:
                        pp.right = cp.left
                    else:
                        pp.left = cp.left
                elif cp.right:
                    if pp_dir:
                        pp.right = cp.right
                    else:
                        pp.left = cp.right
                else:
                    if pp_dir:
                        pp.right = None
                    else:
                        pp.left = None
                return True
        return False

    def search(self, new_data, root=None):
        if not root:
            root = self.root
        cp = root
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
        if not cp:
            return False
        print_list = []

        cp.level = 1
        q = [cp]

        while q:
            node = q.pop(0)
            print_list.append(node)
            if node.left:
                node.left.level = node.level + 1
                q.append(node.left)
            if node.right:
                node.right.level = node.level + 1
                q.append(node.right)

        current_level = 0
        print("LEVEL ORDER TRAVERSAL", end="")
        for node in print_list:
            if current_level == node.level:
                print(node.data, end=" ")
            else:
                print("")
                current_level = node.level
                print('[Level '+str(current_level)+']', end=" ")
                print(node.data, end=" ")


if __name__ == "__main__":
    #data = [8,2,3,1,114,0,-4,17,16,6,9,10,13]
    data = [20,10,40,6,15,30,2,8,18,25,35,7]
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
    print("Perorder: ",end="")
    t.preorder(root)
    print("")
    print("Inorder: ", end="")
    t.inorder(root)
    print("")
    print("Postorder: ", end="")
    t.postorder(root)
    print("")
    #print("LevelOrder: ", end="")
    t.levelorder(root)
    print("")

    print("Want to perform more? [y/n (default n)]: ")
    inp = input().strip()
    if inp != 'y':
        sys.exit()
    print("Do you want to reset tree? [y/n (default n)]: ")
    inp = input().strip()
    if inp == 'y':
        t = BST()
    inp = 1
    while inp:
        print("Enter Desired Option:")
        print("1. Add New Element")
        print("2. Delete Element")
        print("3. Print BST")
        print("4/5/6: preorder/Inorder/Postorder print")
        print("7. Search Element")
        print("0: To exit")
        inp = int(input())
        if inp in range(1, 7):
            if inp == 1:
                print("Enter new integer to add: ")
                d = int(input())
                t.insert_node(d)
            elif inp == 2:
                print("Enter the integer to delete: ")
                d = int(input())
                t.delete_node(d)
            elif inp == 3:
                t.levelorder(t.root)
                print("")
            elif inp == 4:
                print("Perorder: ", end="")
                t.preorder(t.root)
                print("")
            elif inp == 5:
                print("Inorder: ", end="")
                t.inorder(t.root)
                print("")
            elif inp == 6:
                print("Postorder: ", end="")
                t.postorder(t.root)
                print("")
            elif inp == 7:
                print("Enter the element to search: ")
                d = int(input())
                if t.search(d):
                    print("Result: Found")
                else:
                    print("Element not found")