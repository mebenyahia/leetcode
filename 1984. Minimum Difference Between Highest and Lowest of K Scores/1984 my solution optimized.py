'''
Optimized
Runtime: 137 ms, faster than 71.83% of Python3 online submissions for Minimum Difference Between Highest and Lowest of K Scores.
Memory Usage: 14.1 MB, less than 92.01% of Python3 online submissions for Minimum Difference Between Highest and Lowest of K Scores.
'''
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        nums.sort(reverse=True)
        mdiffs = []

        for i in range(len(nums)-k+1):
            mdiffs.append(nums[i]-nums[i+k-1])

        return min(mdiffs)