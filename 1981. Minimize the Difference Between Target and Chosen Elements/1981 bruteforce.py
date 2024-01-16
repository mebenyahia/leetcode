class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        import itertools
        return min([abs(target-sum(i)) for i in list(itertools.product(*mat))])
