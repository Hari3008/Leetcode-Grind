class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hashTable = [0]*26
        for i in range(len(s)):
            hashTable[ord(s[i]) - ord('a')]+=1
            hashTable[ord(t[i]) - ord('a')]-=1
        
        for i in hashTable:
            if i > 0:
                return False
        return True


        # # Hash Map
        # if len(s) != len(t): 
        #     return False
        
        # countS, countT = {}, {}
        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i],0)
        #     countT[t[i]] = 1 + countT.get(t[i],0)
        # return countS == countT
