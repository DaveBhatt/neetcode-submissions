import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque() # stores indices

        l = 0
        for r in range(len(nums)):
            # pop smaller values from right to preserve decreasing order of elements
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # add smaller values at the end (descending order)
            q.append(r)

            # remove leftmost element if out of bounds {e.g (l=4)>(q[-1]=3)}
            if l > q[0]:
                q.popleft()

            # when r exceeds k(window size) start adding elements 
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1 # shift the left pointer

        return res
        
