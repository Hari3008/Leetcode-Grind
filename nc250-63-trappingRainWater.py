class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        leftMax, rightMax = height[l], height[r]

        while l < r:
            # in the condition we'll have to update leftMax since left is on the lower side
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                res += (leftMax - height[l])
            else:
                r-=1
                rightMax =  max(rightMax, height[r])
                res += (rightMax - height[r])
        
        return res
