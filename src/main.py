import random

'''
    AVL Tree

    1. Number에 대한 Binary Tree 입니다.
    2. 기존 Binary Tree에서 불균형으로 인한 시간복접도가
       낮아지는 것을 개선하기 위해 AVL Tree를 이용합니다.
    3. 각 subtree의 rank(height)는 최대 1까지 차이날 수 있습니다.
    4. 중복된 key의 self.insert는 AVL Tree 유지를 위해 존재한다고 표시합니다.
'''

#AVL Tree의 Node Class
class Node:
    def __init__(self, data, height):
        self.data = data
        self.left = None
        self.right = None
        self.height = height

#AVL Tree Class
class AvlTree:
    def __init__(self):
        self.node = None
    
    def search(self, node, key):
        # search Data by using key 
        if node == None:
            return False
        elif node.data == key:
            return True
        elif node.data > key:
            return self.search(node.left, key)
        else :
            return self.search(node.right, key)
    
    def insert(self, node, key):
        # insert data in Tree remaining AVL Tree 
        if self.search(node, key) == True:
            print("Already %d is existed".format(key))
            return node
        if node == None: # Or self == None
            node = Node(key, 1)
            return node
        elif node.data > key:
            node.left = self.insert(node.left, key)
        elif node.data < key:
            node.right = self.insert(node.right, key)

        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        return self.balance(node)

    def delete(self, node, key):
        if self.search(node, key) == False:
            print("Delete data : {} is not existed".format(key))
            return node
        # Delete data in Tree remaining AVL Tree
        if not node:
            return node
        elif node.data > key:
            node.left = self.delete(node.left, key)
        elif node.data < key:
            node.right = self.delete(node.right, key)
        else :
            if node.left is None:
                # 왼쪽 없는 경우 오른쪽 node를 가지고 올라옴
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                # 오른쪽 없는 경우 왼쪽 node를 가지고 올라옴
                temp = node.left
                node = None
                return temp
            # 양쪽 다 있는 경우 오른쪽에서 가장 작은 값을 가져온 다음 balancing
            temp = self.getMinNode(node.right)
            node.data = temp.data
            node.right = self.delete(node.right, temp.data)
        
        if node is None:
            return node
        
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        return self.balance(node)

    def get_height(self, node):
         # Get height start from leaf node, So leaf node height is 0
        if node == None:
            return 0
        return node.height

    def set_height(self, node, cnode):
        # node is parent node, cnode is child node
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        cnode.height = max(self.get_height(cnode.left), self.get_height(cnode.right)) + 1

    def dif_height(self, node):
        # Different height between left and right child for rotate information
        return self.get_height(node.left) - self.get_height(node.right)

    def balance(self, node):
        # Keep AVL Tree structure function
        dif = self.dif_height(node)

        if dif > 1:
            if self.dif_height(node.left) < 0:
                node = self.rotateLR(node)
            else :
                node = self.rotateLL(node)
        elif dif < -1:
            if self.dif_height(node.right) > 0 :
                node = self.rotateRL(node)
            else :
                node = self.rotateRR(node)
        return node

    def rotateLL(self, node):
        # Rotate the left subtree of the left child of the unself.balanced node
        leftnode = node.left
        node.left = leftnode.right
        leftnode.right = node
        self.set_height(node, leftnode)
        return leftnode
        
    def rotateLR(self, node):
        # Rotate the left subtree of the right child of the unself.balanced node     
        node.left = self.rotateRR(node.left)
        node = self.rotateLL(node)
        return node

    def rotateRL(self, node):
        # Rotate the right subtree of the left child of the unself.balanced node
        node.right = self.rotateLL(node.right)
        node = self.rotateRR(node)
        return node

    def rotateRR(self, node):
        # Rotate the right subtree of the right child of the unself.balanced node
        rightnode = node.right
        node.right = rightnode.left
        rightnode.left = node
        self.set_height(node, rightnode)
        return rightnode

    def getMinNode(self, node):
        if node is None or node.left is None:
            return node
        
        return self.getMinNode(node.left)

    def preOrder(self, node):
        if not node:
            print("end ", end="")
            return
        print("{} ".format(node.data), end="")
        self.preOrder(node.left)
        self.preOrder(node.right)

if __name__ == "__main__":
    avlTree = AvlTree() 
    root = None
    for num in range(1, 10): 
        root = avlTree.insert(root, num)

    # Preorder Traversal 
    print("Preorder Traversal") 
    avlTree.preOrder(root) 
    print() 
    
    key = 4
    print()
    print("Search ", end=" ")
    if avlTree.search(root, key):
        print("Data {} is existed".format(key))
    else :
        print("Data {} is not existed".format(key))

    # Delete 
    print()
    root = avlTree.delete(root, key) 
    print()

    # Preorder Traversal 
    print("Preorder Traversal") 
    avlTree.preOrder(root) 
    print()

    print()
    root = None
    avlTree = AvlTree()
    test_list = [i for i in range(1000000)]
    delete_list = random.sample(test_list, 500000)
    print("Start")

    for i in test_list:
        root = avlTree.insert(root, i)
        print(f"{i} complete")
    print("Insertion Complete")
    
    for idx, val in enumerate(delete_list):
        root = avlTree.delete(root, i)
        test_list[val] = -1 # Test for remaining value
        print(f"{val} delete, delete count : {idx}")
    print("Delete Complete")

    remain_answer, remain_wrong, delete_wrong, delete_answer = 0, 0, 0, 0
    print("Start search")
    for idx, val in enumerate(test_list):
        if val >= 0 : 
            # Remaining Test after deletion
            if avlTree.search(root, idx):
                remain_answer += 1
            else :
                remain_wrong += 1
        else :
            # Deletion Test after deleteion
            if avlTree.search(root, idx):
                delete_wrong += 1
            else :
                delete_answer += 1
    print("Search test Complete")

    print(f"Remain Test : answer -> {remain_answer} wrong -> {delete_wrong}")
    print(f"Deletion Test : answer -> {delete_answer} wrong -> {delete_wrong}")
