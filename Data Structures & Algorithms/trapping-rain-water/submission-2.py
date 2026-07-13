class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        max_water = 0
        l ,r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]

        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                max_water += lMax - height[l]

            else:
                r -= 1
                rMax = max(rMax, height[r])
                max_water += rMax - height[r]
        return max_water