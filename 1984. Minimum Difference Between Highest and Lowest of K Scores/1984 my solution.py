'''
Will optimize since I'm not satisfied with performance
'''
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        mdiff = inf

        nums.sort(reverse=True)

        for i in range(len(nums)-k+1):
            mdiff = max(nums[i:k+i])-min(nums[i:k+i]) if max(nums[i:k+i])-min(nums[i:k+i]) < mdiff else mdiff

        return mdiff