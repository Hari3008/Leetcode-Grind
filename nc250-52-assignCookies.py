class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        cookie = kid = 0
        # Traverse through the kids array
        while kid < len(g):
            # keep comparing until kid lesser than cookie size
            while cookie < len(s) and g[kid] > s[cookie]:
                cookie+=1
            
            if cookie == len(s):
                return kid
            kid+=1
            cookie+=1
        
        return kid
