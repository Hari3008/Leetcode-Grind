
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = collections.deque()
        q.append(root)
        res.append(root.val)

        while q:
            qLen = len(q)
            rightmost = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    if node.left:
                        rightmost.append(node.left.val)
                    if node.right:
                        rightmost.append(node.right.val)
            
            if rightmost:
                res.append(rightmost[-1])
                # res.append(q[-1].val)
        
        return res
