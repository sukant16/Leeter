from typing import List
import itertools

from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        max_time = -1

        for h, i, j, k in permutations(A):
            hours = h*10 + i
            minutes = j*10 + k
            if hours < 24 and minutes < 60:
                max_time = max(max_time, hours*60 + minutes)
        if max_time != -1:
            return '{:02d}:{:02d}'.format(max_time//60, max_time%60)
        else:
            return ""

    def largestTimeFromDigits2(self, A):
        return max(["%d%d:%d%d" % t for t in itertools.permutations(A) if t[:2] < (2, 4) and t[2] < 6] or [""])


if __name__== "__main__":
    sol = Solution()
    ans1 = sol.largestTimeFromDigits2([1, 2, 6, 4])
    ans2 = sol.largestTimeFromDigits2([2, 0, 6, 6])
    print(ans1, ans2)
    assert ans1 == "21:46", "bad"
    assert ans2 == "06:26", "bad"
