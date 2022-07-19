'''
We are looking for indices that satisfy abs(i - j) <= k
We know that:
	- i and j are strictly positive 
	- j is equal to i + a constant
so:
since j = i + c, then abs(i - j) = abs(i - (i + c)) = abs(c) <= k
The two distinct indices will always be separated by a dynamic window that is at most of size k. 

for nums = [1, 2, 3, 1], k = 3 is true because nums[3] == nums [0] and abs(3 - 0) <= 3 
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:


        for i in range(len(nums)):
            for j in range(1, k+1):
                if i+j <= len(nums)-1:
                    if nums[i] == nums[i+j]:
                        return True
                else:
                    break


        return False

