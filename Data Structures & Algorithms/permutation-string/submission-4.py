class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charCount = {}
        for i in range(len(s1)):
            charCount[s1[i]] = 1 + charCount.get(s1[i], 0)
        
        l = 0
        for r in range(len(s2)):
            charCount[s2[r]] = charCount.get(s2[r], 0) - 1

            while charCount[s2[r]] < 0:
                charCount[s2[l]] = charCount.get(s2[l], 0) + 1
                l += 1
            
            if (r - l + 1) == len(s1):
                return True
        return False 