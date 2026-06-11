class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights) - 1):
            for j in range(i+1, len(heights)):
                area = min(heights[i], heights[j]) * (j - i)
                max_area = max(area, max_area)
        return max_area

        