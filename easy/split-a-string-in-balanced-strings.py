'''
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.



Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
'''


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = out = 0
        for c in s:
            if c == 'R':
                count += 1
            else:
                count -= 1
            if count == 0:
                out += 1
        return out

        # Better solution above (from another leetcode user")
        # i = count = 0
        # j = 2
        # while i < len(s)-1:
        #     if s[i:i+j].count('R') == s[i:i+j].count('L'):
        #         count += 1
        #         i += j
        #         j = 2
        #     else:
        #         j += 2
        #
        # return count


if __name__=="__main__":

    sol = Solution()
    ans1 = sol.balancedStringSplit("RLRRLLRLRL")
    assert (ans1 == 4), 'wrong'

    ans2 = sol.balancedStringSplit("RLLLLRRRLR")
    assert (ans2 == 3), 'wrong'