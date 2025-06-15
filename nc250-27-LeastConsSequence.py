class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Brute Force
        # if len(nums) == 0:
        #     return 0
        # nums = list(set(nums))
        # nums.sort()
        # max_len = 1
        # length = 1
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]+1:
        #         length+=1
        #         max_len = max(length,max_len)
        #     else:
        #         length = 1
        # return max_len

        # Hash map
        mp = defaultdict(int)

        res = 0
        for num in nums:
            if not mp[num]:
                mp[num] = 1 + mp[num-1] + mp[num+1]
                mp[num + mp[num+1]] = mp[num]
                mp[num - mp[num-1]] = mp[num]
                res = max(res,mp[num])
        return res
