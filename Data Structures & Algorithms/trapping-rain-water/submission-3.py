class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        max_water = 0
        l, r = 0, len(height)-1
        maxl, maxr = height[l], height[r]

        while l<r:
            if maxl < maxr:
                l += 1
                maxl = max(maxl, height[l])
                max_water += maxl - height[l]
            else:
                r -= 1
                maxr = max(maxr, height[r])
                max_water += maxr - height[r]
        return max_water