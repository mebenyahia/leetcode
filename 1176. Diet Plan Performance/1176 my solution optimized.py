'''
Runtime: 210 ms, faster than 96.40% of Python3 online submissions for Diet Plan Performance.
Memory Usage: 23.3 MB, less than 31.53% of Python3 online submissions for Diet Plan Performance.
'''
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        s = sum(calories[0:k])
        step = 0

        points = 1 if s>upper else -1 if s<lower else 0


        for i in range(k, len(calories)):
            s = s - calories[step] + calories[i]
            step += 1

            if s>upper:
                points += 1

            if s<lower:
                points -= 1


        return points
