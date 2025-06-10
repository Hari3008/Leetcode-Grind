class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hashmap = defaultdict(int) # incoming - outgoing = n - 1

        for i,o in trust:
            hashmap[i]-=1
            hashmap[o]+=1
        
        for i in range(1,n+1):
            if hashmap[i] == n - 1:
                return i
        
        return -1
