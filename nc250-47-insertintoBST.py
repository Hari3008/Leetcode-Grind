# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # Recursive Approach
        if not root:
            return TreeNode(val)
        
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        return root




        
        # Iterative Approach - Basically traverse through the left or right suybtree by comparing the value, if you hit a leaf node, then create a new node with val and return root
        if not root:
            return TreeNode(val)

        cur = root
        while True:
            if cur.val < val:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                cur = cur.right
            else:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                cur = cur.left
