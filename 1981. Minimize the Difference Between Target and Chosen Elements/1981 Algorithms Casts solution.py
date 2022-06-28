'''Algorithm casts solution
'''
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        smallestSum = sum(min(row) for row in mat)
        if smallestSum > target:
            return smallestSum - target
        S = {0}
        for row in mat:
            S = { s + a for a in row for s in S if s + a <= 2*target - smallestSum}
        return min(abs(target-s) for s in S)