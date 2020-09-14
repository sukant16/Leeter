'''
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]

Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        for interval in intervals:

            # new interval is after the current interval
            if interval[1] < newInterval[0]:
                ans.append(interval)

            # new interval is before the current interval
            # append the new interval to answer
            # update the current interval to new one
            elif interval[0] > newInterval[1]:
                ans.append(newInterval)
                newInterval = interval

            # new interval overlaps with the current interval
            # strech the newinterval to include the overlapped region
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        ans.append(newInterval)
        return ans

class Saubhik:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = False
        ans = []

        for interval in intervals:
            if merged:
                ans.append(interval)

            # ends before start of current interval
            elif newInterval[1] < interval[0]:
                ans.append(newInterval)
                ans.append(interval)
                merged = True

            # ends between start and end of current interval
            elif interval[0] <= newInterval[1] <= interval[1]:
                interval[0] = min(interval[0], newInterval[0])
                ans.append(interval)
                merged = True

            # starts between start and end of current interval
            elif interval[0] <= newInterval[0] <= interval[1]:
                newInterval = [interval[0], max(newInterval[1], interval[1])]

            # starts after end of current interval
            elif interval[1] < newInterval[0]:
                ans.append(interval)

        if not merged:
            ans.append(newInterval)

        return ans



