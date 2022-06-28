'''
My solution
Accumulate the number of sums from the left and from the right
if there is a match in the array at the same index, return that index
if not return -1
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        a = list(accumulate(nums))
        b = list(accumulate(nums[::-1]))[::-1]
        for i in range(0, len(nums)):
	        if a[i] == b[i]:
		        return i
        return -1
