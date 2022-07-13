'''
Optimized solution :)  
Implementation without a deque, slightly faster
I think there might a relation between cnt i and popleft

Runtime: 406 ms, faster than 24.01% of Python3 online submissions for Minimum Size Subarray Sum.
Memory Usage: 27.1 MB, less than 18.33% of Python3 online submissions for Minimum Size Subarray Sum.

'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mix = float('inf')
        cnt = 0
        s = 0
        popleft = 0

        for i in range(len(nums)):
            if s < target:
                cnt += 1
                s += nums[i]

            while s >= target:
                if mix > cnt:
                    mix = cnt
                cnt -= 1
                s -= nums[popleft]
                popleft += 1


        return mix if mix != float('inf') else 0