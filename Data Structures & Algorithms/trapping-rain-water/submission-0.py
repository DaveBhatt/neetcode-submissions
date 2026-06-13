class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: return 0

        max_water = 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]


        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                max_water += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                max_water += rightMax - height[r]
        return max_water
