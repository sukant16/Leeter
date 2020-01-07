from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time, last_point = 0, points[0]
        for point in points:
            time += max(abs(point[0]-last_point[0]),
                        abs(point[1]-last_point[1]))
            last_point = point
        return time


if __name__=='__main__':

    sol = Solution()

    ans1 = sol.minTimeToVisitAllPoints(points = [[1,1],[3,4],[-1,0]])
    assert (ans1==7), 'wrong'

    ans2 = sol.minTimeToVisitAllPoints([[3,2],[-2,2]])
    assert (ans2==5), 'wrong'