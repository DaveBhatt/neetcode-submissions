class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0 or len(t) > len(s): 
            return ""
            
        CountT = {}
        for char in t:
            CountT[char] = 1 + CountT.get(char, 0)
            
        have = 0
        need = len(CountT)
        window = {}
        
        # Add variables to track the minimum window boundaries and its length
        res = [-1, -1] 
        resLen = float("infinity")
        
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)
            
            # Only increment 'have' if the character is in 't' and we've met the exact frequency
            if char in CountT and window[char] == CountT[char]:
                have += 1
                
            while have == need:
                # 1. Record the current window if it's the smallest we've seen so far
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                    
                # 2. Shrink the window from the left
                left_char = s[l]
                window[left_char] -= 1
                
                # 3. If the removed character is in 't' and it causes our window to fall short, decrement 'have'
                if left_char in CountT and window[left_char] < CountT[left_char]:
                    have -= 1
                    
                l += 1
                
        # Return the substring if a valid window was found, otherwise return an empty string
        l, r = res
        return s[l : r + 1]
