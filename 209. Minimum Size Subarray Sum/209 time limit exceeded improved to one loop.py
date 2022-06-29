'''
Still time limit exceeded but one loop amirite
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        k = 1
        start = 0
        smallestsize = float('inf')

        while(k<len(nums)):
            if nums[start] >= target:
                return 1

            if sum(nums[start:k+1]) >= target:
                if len(nums[start:k+1]) < smallestsize:
                    smallestsize = len(nums[start:k+1])
                start += 1


            elif k<len(nums):
                k+= 1

        return smallestsize if smallestsize != float('inf') else 0



        


        