class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in prevMap:
                return[prevMap[diff], i+1]
            prevMap[n] = i+1
        return

        