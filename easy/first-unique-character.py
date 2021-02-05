"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.

"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for idx, ch in enumerate(s):
            if d[ch] == 1:
                return idx

        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.firstUniqChar("leetcode"))
    print(sol.firstUniqChar("loveleetcode"))



