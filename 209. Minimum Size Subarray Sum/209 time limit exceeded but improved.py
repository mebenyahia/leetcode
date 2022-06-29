'''
Improved but time limit still exceeded
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minsize = float('inf')
        k = 1
        start = 0
        while(k < len(nums)+1 and start != k):
            while (sum(nums[start:k]) >= target):
                if len(nums[start:k])<= minsize:
                    minsize = len(nums[start:k])
                start += 1

            k += 1
            
            if minsize == 1:
                return minsize


        return minsize if minsize != float('inf') else 0
