class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0 or len(t) > len(s) : return ""
        CountT = {}
        for char in t:
            CountT[char] = 1 + CountT.get(char, 0)
        
        have = 0
        need = len(CountT)
        window = {}

        res = [-1, -1]
        resLen = float("infinity")
        l = 0

        for r in range(len(s)):
            
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in CountT and window[s[r]] == CountT[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in CountT and window[s[l]] < CountT[s[l]]:
                    have -= 1

                l += 1

        l, r = res
        return s[l : r + 1]