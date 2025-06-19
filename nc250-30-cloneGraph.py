"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#######
#### BFS
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        oldtoNewDict = {}
        oldtoNewDict[node] = Node(node.val)
        q = deque([node])

        while q:
            current = q.popleft()
            for neighbor in current.neighbors:
                if neighbor not in oldtoNewDict:
                    oldtoNewDict[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                oldtoNewDict[current].neighbors.append(oldtoNewDict[neighbor])
        
        return oldtoNewDict[node]

###############
#### DFS

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        oldtoNewDict = {}
        oldtoNewDict[node] = Node(node.val)
        q = deque([node])

        while q:
            current = q.popleft()
            for neighbor in current.neighbors:
                if neighbor not in oldtoNewDict:
                    oldtoNewDict[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                oldtoNewDict[current].neighbors.append(oldtoNewDict[neighbor])
        
        return oldtoNewDict[node]
