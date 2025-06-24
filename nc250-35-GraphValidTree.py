class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False
        
        adjList = { i:[] for i in range(n)}

        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)    
        
        visit = set()
        def dfs(i, prev):
            if i in visit: # Cycle Detected
                return False
            
            visit.add(i)
            for j in adjList[i]:
                if j == prev: # To skip the previous node since we already used that node
                    continue
                
                if not dfs(j,i):
                    return False
            
            return True
        
        return dfs(0,-1) and len(visit) == n # to check for cycle and connected graph
