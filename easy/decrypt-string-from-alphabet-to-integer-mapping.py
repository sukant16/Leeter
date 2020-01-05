'''
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.
'''


class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ''
        i = 0
        while (i < len(s)):
            if (len(s) > 2) and ('#' in s[i :i+3]):
                ans += chr(int(s[i: i+2]) -1 + ord('a'))
                i += 3
            else:
                ans += chr(int(s[i: i+1]) -1 + ord('a'))
                i += 1
        return ans

if __name__=='__main__':
    sol = Solution()
    ans1 = sol.freqAlphabets(s="25#")
    assert (ans1 == 'y'), 'wrong logic'
    ans2 = sol.freqAlphabets(s="10#11#12")
    assert (ans2 == 'jkab'), 'wrong logic'