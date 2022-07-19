'''
Fairly fast..
Brought to my attention my dumbness when it comes to indexes lol
'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        maximum = s = sum(nums[0:k])
        upperbound = len(nums)-k


        for i in range(upperbound):
            s = s - nums[i] + nums[k+i]
            if maximum < s:
                maximum = s

        return maximum/k