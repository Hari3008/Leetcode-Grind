class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adjList = [ [] for _ in range(n+1)]

        def dfs(node, prev):
            if visit[node]:
                return True
            
            visit[node] = True
            for nei in adjList[node]:
                if nei == prev:
                    continue
                if dfs(nei,node):
                    return True
            return False
        # Go throuh each edge, Have a clean visit set for each edge checked
        # It makes sense since if you make visit global, then it would return True once every node is visited.
        # have a prev node as well
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            visit = [False] * (n+1)

            if dfs(u,-1):
                return [u,v]
        
        return []
