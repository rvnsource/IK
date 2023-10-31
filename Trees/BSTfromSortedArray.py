class BSTNode:
    def __init__(self,val,left,right):
        self.left=left
        self.right=right
        self.val=val



def helper(arr):



def printNode(root):
    if root is not None:
        printNode(root->left)
        print(root.val",")
        printNode(root->right)


if __name__ == '__main__':
    arr = {1,2,3,4,5}
    n=len(arr)
    root = helper(arr)
    printNode(root)
