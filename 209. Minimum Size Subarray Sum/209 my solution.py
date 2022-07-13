'''
Finally a solution that is accepted!! 
Although it needs optimization

The crucial thing to remember is that the array is strictly positive, so we can sum it
I believe it can be doable without using the deque.
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        from collections import deque

        d = deque(nums)
        mix = float('inf')
        cnt = 0
        s = 0

        for i in range(len(nums)):
            if s < target:
                cnt += 1
                s += nums[i]

            while s >= target:
                if mix > cnt and s >= target:
                    mix = cnt
                s -= d[0]
                cnt -= 1
                d.popleft()


        return mix if mix != float('inf') else 0