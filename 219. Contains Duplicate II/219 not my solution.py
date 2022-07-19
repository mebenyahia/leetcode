'''
Check if the element j is in the dictionary, and then if the index of that element (distinct) is different than the one of j in the dict.
If j isn't in the dict, enter in dictionary
Not my solution, but thank you kengni on Leetcode! 
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dic = {}
        for i, j in enumerate(nums):
            if j in dic and i - dic[j] <= k:
                return True
            dic[j] = i

        return False
