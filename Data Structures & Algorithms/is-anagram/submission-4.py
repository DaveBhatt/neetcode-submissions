class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countS[t[i]] = countS.get(t[i], 0) - 1
        for c in countS:
            if countS[c] != 0:
                return False
        return True