class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countChar = {}
        res = 0
        l = 0

        for r in range(len(s)):
            countChar[s[r]] = 1 + countChar.get(s[r], 0)

            window_size = r - l + 1            
            while window_size - max(countChar.values()) > k:
                countChar[s[l]] -= 1
                l += 1
                window_size -= l
            res = max(res, window_size)
        return res