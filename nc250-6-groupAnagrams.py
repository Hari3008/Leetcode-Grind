class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # # Sorting approach
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())


        # Hash Table
        # Basically create a hash table with 26 zeros (alphabets)
        # Add all the strings which associate with that hashtable
        res = defaultdict(list)
        for s in strs:
            hash_table = [0]*26
            for ch in s:
                hash_table[ord(ch) - ord('a')]+=1
            res[tuple(hash_table)].append(s)
        return list(res.values())
      
