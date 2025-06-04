class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicateSet = set()
        for i in nums:
            if i in duplicateSet:
                return True
            duplicateSet.add(i)
        return False
