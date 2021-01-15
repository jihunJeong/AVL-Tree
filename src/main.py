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
        self.root = None
    
    def search(self, key):
        # search Data by using key 
        if self.root == key:
            return key
        elif self.root.data > key:
            return search(self.root.left, key)
        else :
            return search(self.root.right, key)
    
    def insert(self, key):
        # insert data in Tree remaining AVL Tree

    def delete():
        # delete data in Tree remaining AVL Tree
    
    def getHeight():


    # Rotate the left subtree of the left child of the unbalanced node
    def rotateLL():
        
    # Rotate the left subtree of the right child of the unbalanced node     
    def rotateRL():
    
    # Rotate the right subtree of the left child of the unbalanced node
    def rotateLR():
    
    # Rotate the right subtree of the right child of the unbalanced node
    def rotateRR():

if __name__ == "__main__":