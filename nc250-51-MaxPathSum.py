# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # with branch splitting
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # Return without splitting because if you return with split it wont be a [path]
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]
