'''
Exceeds time limit
'''
class Solution:
    def minSubArrayLen(self, target: int, arr: List[int]) -> int:
        k = 1
        start = 0
        maxi = float('inf')
        for k in range(len(arr)+1):
            if sum(arr[start:k]) >= target :
                while(sum(arr[start:k]) >= target):
                    if len(arr[start:k]) < maxi:
                        maxi = len(arr[start:k])
                    start += 1

        return maxi if maxi != float('inf') else 0

