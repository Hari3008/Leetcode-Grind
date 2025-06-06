class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Extension of Permutation 1 but just appended the permutations to the set so that it can avoid duplicates
        # Use a hashset
        if len(nums) == 0:
            return [[]]

        res = set()
        perm = self.permuteUnique(nums[1:])

        for p in perm:
            for i in range(len(p)+1):
                pcopy = p.copy()
                pcopy.insert(i,nums[0])
                res.add(tuple(pcopy))
        
        return [list(p) for p in res]

