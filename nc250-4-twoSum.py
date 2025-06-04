class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSumDict = {}
        for i in range(len(nums)):
            if (target - nums[i]) in twoSumDict:
                return [twoSumDict[target - nums[i]],i]
            twoSumDict[nums[i]] = i
        return []
