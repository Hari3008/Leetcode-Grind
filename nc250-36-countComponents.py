class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[]for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(node):
            for nei in adjList[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        
        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res+=1

        return res
