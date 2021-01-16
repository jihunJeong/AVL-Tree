'''
    AVL Tree

    1. Number에 대한 Binary Tree 입니다.
    2. 기존 Binary Tree에서 불균형으로 인한 시간복접도가
       낮아지는 것을 개선하기 위해 AVL Tree를 이용합니다.
    3. 각 subtree의 rank(height)는 최대 1까지 차이날 수 있습니다.
    4. 중복된 key의 Insert는 AVL Tree 유지를 위해 존재한다고 표시합니다.
'''

#AVL Tree의 Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#AVL Tree Class
class AVL_Tree:
    def __init__(self):
        self.node = None
        self.height = 0
    
    def search(self, key):
        # search Data by using key 
        if self.node == key:
            return True
        elif self.height == 0:
            return False
        elif self.node.data > key:
            return search(self.node.left, key)
        else :
            return search(self.node.right, key)
    
    # Insert data in Tree remaining AVL Tree 
    def insert(self, key):
        if search(key) == True:
            print("Already %d is existed".format(key))
        cnode = self.node # Current Node
        if cnode == None: # Or self == None
            node = Node(key)
            cnode = node
        elif cnode.data > key:
            insert(cnode.left, key)
        else :
            insert(cnode.right, key)
        balance()

    # Delete data in Tree remaining AVL Tree
    def delete(self, key):
        
    # Get height start from leaf node, So leaf node height is 0
    def getHeight(self):
        # if 
        self.height = max()
    def balance(self):

    # Rotate the left subtree of the left child of the unbalanced node
    def rotateLL():
        
    # Rotate the left subtree of the right child of the unbalanced node     
    def rotateRL():
    
    # Rotate the right subtree of the left child of the unbalanced node
    def rotateLR():
    
    # Rotate the right subtree of the right child of the unbalanced node
    def rotateRR():

if __name__ == "__main__":