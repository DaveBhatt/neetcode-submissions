class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # HashMap Technique
        s1CharCounter = {}
        for char in s1:
            s1CharCounter[char] = 1 + s1CharCounter.get(char, 0)

        l = 0
        for r in range(len(s2)):
            s1CharCounter[s2[r]] = s1CharCounter.get(s2[r], 0) - 1

            while s1CharCounter[s2[r]] < 0:
                s1CharCounter[s2[l]] += 1  #make charCount +ve before sliding window
                l += 1

            if (r - l + 1) == len(s1):
                return True
        return False