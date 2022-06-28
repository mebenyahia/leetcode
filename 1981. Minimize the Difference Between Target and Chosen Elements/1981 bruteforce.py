'''
Brute force solution
Exceeds Memory Limit

Algo: Generate all possible product combinations for list mat, then compute the absolute difference between the target and the sum of each. 
Then return the minimum.
'''
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        import itertools
        return min([abs(target-sum(i)) for i in list(itertools.product(*mat))])
