'''
Took me long enough
I think the proper way now is; book -> work through by topic
Runtime: 79 ms, faster than 79.24% of Python3 online submissions for Two Sum.
Memory Usage: 15.1 MB, less than 50.46% of Python3 online submissions for Two Sum.

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        
        for i, j in enumerate(nums):
            if target - j in dic:
                return [i, dic[target - j]]
            dic[j] = i
                